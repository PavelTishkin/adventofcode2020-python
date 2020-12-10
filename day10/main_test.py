import unittest

from day10 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11,
                         1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        main.add_jolts_min_max(self.adapters)

    def test_count_jolt_diffs_returns_correct_diffs_small(self):
        adapters_small = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        main.add_jolts_min_max(adapters_small)
        adapters_small.sort()
        actual = main.count_jolt_diffs(adapters_small, 1, 3)
        self.assertEqual(actual['1'], 7)
        self.assertEqual(actual['3'], 5)

    def test_count_jolt_diffs_returns_correct_diffs(self):
        self.adapters.sort()
        actual = main.count_jolt_diffs(self.adapters, 1, 3)
        self.assertEqual(actual['1'], 22)
        self.assertEqual(actual['3'], 10)

    def test_get_contiguous_map_of_ones_returns_correct_counts(self):
        adapters_small = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        main.add_jolts_min_max(adapters_small)
        adapters_small.sort()
        actual = main.get_contiguous_map_of_ones(adapters_small)
        self.assertEqual(actual[0], 3)
        self.assertEqual(actual[1], 2)

    def test_is_valid_permutation_returns_true_on_valid(self):
        actual = main.is_valid_permutation([1, 0, 1, 1, 0])
        self.assertTrue(actual)

    def test_is_valid_permutation_returns_false_on_invalid(self):
        actual = main.is_valid_permutation([1, 0, 1, 1, 1])
        self.assertFalse(actual)

    def test_get_valid_permutations_len_returns_correct_count(self):
        actual = main.get_valid_permutations_len(5)
        self.assertEqual(actual, 13)

    def test_all_valid_permutations_count_small(self):
        adapters_small = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        main.add_jolts_min_max(adapters_small)
        adapters_small.sort()
        ones_map = main.get_contiguous_map_of_ones(adapters_small)
        actual = 1
        for ones in ones_map:
            actual *= main.get_valid_permutations_len(ones)
        self.assertEqual(actual, 8)

    def test_all_valid_permutations_count(self):
        self.adapters.sort()
        ones_map = main.get_contiguous_map_of_ones(self.adapters)
        actual = 1
        for ones in ones_map:
            actual *= main.get_valid_permutations_len(ones)
        self.assertEqual(actual, 19208)
