import unittest

from day9 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 57]

    def test_is_valid_sum_detects_correct_sum(self):
        self.assertTrue(main.is_valid_sum(self.numbers[0:5], self.numbers[5]))

    def test_is_valid_sum_detects_incorrect_sum(self):
        self.assertFalse(main.is_valid_sum(self.numbers[9:14], self.numbers[14]))

    def test_find_rule_exception(self):
        actual = main.find_weak_number(self.numbers, 5)
        self.assertEqual(actual, 127)

    def test_sum_array_return_correct_sum(self):
        actual = main.sum_array(self.numbers[2:6])
        self.assertEqual(actual, 127)

    def test_encryption_weakness_finds_result(self):
        actual = main.find_encryption_weakness(self.numbers, 127)
        self.assertEqual(actual, 62)
