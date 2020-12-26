import unittest

import numpy

from day23 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cup_sequence = [int(n) for n in list('389125467')]

    def test_cup_move_returns_correct_sequence(self):
        actual = main.cup_move(self.cup_sequence)
        self.assertEqual(actual, [2, 8, 9, 1, 5, 4, 6, 7, 3])

    def test_multiple_cup_move_returns_correct_sequence(self):
        actual = self.cup_sequence
        for i in range(10):
            actual = main.cup_move(actual)
        self.assertEqual(actual, [8, 3, 7, 4, 1, 9, 2, 6, 5])

    def test_cup_shift_sequence_returns_correct_sequence(self):
        actual = main.cup_shift_sequence([8, 3, 7, 4, 1, 9, 2, 6, 5], 1)
        self.assertEqual(actual, [9, 2, 6, 5, 8, 3, 7, 4])

    def test_generate_sequence_to_number_returns_correct_sequence(self):
        actual = main.generate_sequence_to_number([5, 4, 3, 2, 1], 1000000)
        self.assertEqual(actual[5], 6)
        self.assertIn(1000000, actual)
        self.assertEqual(len(actual), 1000000)

    def test_cup_move_v2_returns_correct_sequence(self):
        sequence = numpy.array(self.cup_sequence)
        curr_idx = 0
        for i in range(10):
            sequence, curr_idx = main.cup_move_v2(sequence, curr_idx, 9)
        sequence = main.cup_shift_sequence(sequence.tolist(), 1)
        self.assertEqual(sequence, [9, 2, 6, 5, 8, 3, 7, 4])

    def test_generate_sequence_cup_move_produces_same_result(self):
        old_sequence = numpy.array([3, 8, 9, 1, 2, 5, 4, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        curr_idx = 0
        for i in range(100):
            old_sequence, curr_idx = main.cup_move_v2(old_sequence, curr_idx, 20)

        new_sequence = main.generate_sequence_to_number(self.cup_sequence, 20)
        curr_idx = 0
        for i in range(100):
            new_sequence, curr_idx = main.cup_move_v2(new_sequence, curr_idx, 20)
        self.assertEqual(list(old_sequence), list(new_sequence))

    def test_large_cup_move_returns_correct_sequence(self):
        sequence = main.generate_sequence_to_number(self.cup_sequence, 1000000)
        curr_idx = 0
        for i in range(10000000):
            sequence, curr_idx = main.cup_move_v2(sequence, curr_idx, 1000000)
        first_cup_idx = [i for i in range(len(sequence)) if sequence[i] == 1][0]
        sequence = main.cup_shift_sequence_v2(sequence, first_cup_idx)

        self.assertEqual(sequence[1] * sequence[2], 149245887792)
