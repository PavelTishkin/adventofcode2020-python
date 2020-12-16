import unittest

from day15 import main


class MainTestCase(unittest.TestCase):

    def test_get_next_number_finds_correct_new_number(self):
        num_seq = [0, 3, 6]
        next_number = main.get_next_number(num_seq)
        self.assertEqual(next_number, 0)

    def test_get_next_number_finds_correct_repeat_number(self):
        num_seq = [0, 3, 6, 0]
        next_number = main.get_next_number(num_seq)
        self.assertEqual(next_number, 3)

    def test_get_numbers_sequence_returns_correct_sequence1(self):
        num_seq = [0, 3, 6]
        actual = main.get_nth_number_with_lookup(num_seq, 2020)
        self.assertEqual(actual, 436)

    def test_get_numbers_sequence_returns_correct_sequence2(self):
        num_seq = [1, 3, 2]
        actual = main.get_nth_number_with_lookup(num_seq, 2020)
        self.assertEqual(actual, 1)

    def test_get_numbers_sequence_returns_correct_sequence3(self):
        num_seq = [2, 1, 3]
        actual = main.get_nth_number_with_lookup(num_seq, 2020)
        self.assertEqual(actual, 10)

    def test_get_numbers_sequence_returns_correct_sequence4(self):
        num_seq = [1, 2, 3]
        actual = main.get_nth_number_with_lookup(num_seq, 2020)
        self.assertEqual(actual, 27)

    def test_get_numbers_sequence_returns_correct_sequence5(self):
        num_seq = [2, 3, 1]
        actual = main.get_nth_number_with_lookup(num_seq, 2020)
        self.assertEqual(actual, 78)

    def test_get_numbers_sequence_returns_correct_sequence6(self):
        num_seq = [3, 2, 1]
        actual = main.get_nth_number_with_lookup(num_seq, 2020)
        self.assertEqual(actual, 438)

    def test_get_numbers_sequence_returns_correct_sequence7(self):
        num_seq = [3, 1, 2]
        actual = main.get_nth_number_with_lookup(num_seq, 2020)
        self.assertEqual(actual, 1836)

    def test_init_lookup_initializes_correct_values(self):
        num_seq = [0, 3, 6]
        actual = main.init_lookup(num_seq)
        self.assertEqual(actual[0], 0)
        self.assertEqual(actual[3], 1)
        self.assertEqual(actual[6], 2)

    def test_get_next_number_with_lookup_returns_correct_value_when_value_is_new(self):
        num_seq = [0, 3, 6]
        lookup = main.init_lookup(num_seq[:-1])
        actual = main.get_next_number_with_lookup(num_seq[-1], 2, lookup)
        self.assertEqual(actual, 0)

    def test_get_next_number_with_lookup_updates_lookup_when_value_is_new(self):
        num_seq = [0, 3, 6]
        lookup = main.init_lookup(num_seq[:-1])
        self.assertNotIn(2, lookup)
        main.get_next_number_with_lookup(num_seq[-1], 2, lookup)
        self.assertEqual(lookup[6], 2)

    def test_get_next_number_with_lookup_returns_correct_value_when_value_exists(self):
        num_seq = [0, 3, 6]
        lookup = main.init_lookup(num_seq[:-1])
        new_num = main.get_next_number_with_lookup(num_seq[-1], 2, lookup)
        actual = main.get_next_number_with_lookup(new_num, 3, lookup)
        self.assertEqual(actual, 3)

    def test_get_next_number_with_lookup_updates_lookup_when_value_exists(self):
        num_seq = [0, 3, 6]
        lookup = main.init_lookup(num_seq[:-1])
        self.assertNotIn(2, lookup)
        new_num = main.get_next_number_with_lookup(num_seq[-1], 2, lookup)
        main.get_next_number_with_lookup(new_num, 3, lookup)
        print(lookup)
        self.assertEqual(lookup[0], 3)

    def test_large_get_numbers_sequence_returns_correct_sequence1(self):
        num_seq = [0, 3, 6]
        actual = main.get_nth_number_with_lookup(num_seq, 30000000)
        self.assertEqual(actual, 175594)
