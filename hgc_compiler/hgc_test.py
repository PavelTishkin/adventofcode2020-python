import unittest

from hgc_compiler.hgc import Instruction, HandheldGameConsole


class HandheldGameConsoleTestCase(unittest.TestCase):

    def test_parse_instruction(self):
        instruction = Instruction()
        instruction.parse_instruction("nop +0")
        self.assertEqual(instruction.action, "nop")
        self.assertEqual(instruction.parameter1, 0)

    def test_hgc_load_instructions(self):
        text_instructions = [
            "nop +0",
            "acc +1",
            "jmp +4"
        ]
        hgc = HandheldGameConsole()
        hgc.load_instructions(text_instructions)
        self.assertEqual(len(hgc.instructions), 3)
        self.assertEqual(hgc.instructions[1].action, "acc")
        self.assertEqual(hgc.instructions[1].parameter1, 1)

    def test_hgc_infinite_loop(self):
        text_instructions = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"
        ]
        hgc = HandheldGameConsole()
        hgc.load_instructions(text_instructions)
        hgc.run()
        self.assertEqual(hgc.termination, "inf_loop")
        self.assertEqual(hgc.acc, 5)

    def test_hgc_infinite_loop_recover(self):
        text_instructions = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"
        ]
        hgc = HandheldGameConsole()
        hgc.load_instructions(text_instructions)
        hgc.run()
        hgc.reset()
        hgc.get_instructions()[7].set_action('nop')
        hgc.run()
        self.assertEqual(hgc.termination, "standard")
        self.assertEqual(hgc.acc, 8)
