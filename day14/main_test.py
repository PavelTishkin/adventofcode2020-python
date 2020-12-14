import unittest

from day14 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.instructions = [
            'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
            'mem[8] = 11',
            'mem[7] = 101',
            'mem[8] = 0'
        ]
        self.programs = main.load_instructions_into_programs(self.instructions)

        self.quantum_instructions = [
            'mask = 000000000000000000000000000000X1001X',
            'mem[42] = 100',
            'mask = 00000000000000000000000000000000X0XX',
            'mem[26] = 1'
        ]
        self.quantum_programs = main.load_instructions_into_programs(self.quantum_instructions)

    def test_update_memory_assigns_correct_value_to_memory(self):
        memory = {}
        program = self.programs[0]
        main.update_memory(program['mask'], program['commands'][0], memory)
        self.assertEqual(memory[8], 73)

    def test_run_program_assigns_correct_values_to_memory(self):
        memory = {}
        main.run_program(self.programs[0], memory)
        self.assertTrue(memory[7], 101)
        self.assertTrue(memory[8], 64)

    def test_get_quantum_memory_address_values_contains_correct_values(self):
        mem_values = []
        main.get_quantum_memory_address_values('000000000000000000000000000000X1101X', mem_values)
        self.assertIn(26, mem_values)
        self.assertIn(27, mem_values)
        self.assertIn(58, mem_values)
        self.assertIn(59, mem_values)

    def test_run_quantum_program_initializes_correct_memory_values(self):
        memory = {}
        main.run_program(self.quantum_programs[1], memory, 2)
        self.assertEqual(memory[16], 1)
        self.assertEqual(memory[17], 1)
        self.assertEqual(memory[18], 1)
        self.assertEqual(memory[19], 1)
        self.assertEqual(memory[24], 1)
        self.assertEqual(memory[25], 1)
        self.assertEqual(memory[26], 1)
        self.assertEqual(memory[27], 1)

    def test_get_quantum_memory_sum_returns_correct_sum(self):
        memory = {}
        main.run_programs(self.quantum_programs, memory, 2)
        actual = main.get_memory_sum(memory)
        self.assertEqual(actual, 208)
