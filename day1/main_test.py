import unittest

from day1 import main


class MainTestCase(unittest.TestCase):

    def test_sum_check_two_numbers_start_pass(self):
        # Selected numbers are 4 and 19
        input_list = [4, 8, 19, 55, 9]
        actual = main.sum_check(input_list, 23, 2, [])
        self.assertEqual(actual, 76)

    def test_sum_check_two_numbers_middle_pass(self):
        # Selected numbers are 8 and 19
        input_list = [4, 8, 19, 55, 9]
        actual = main.sum_check(input_list, 27, 2, [])
        self.assertEqual(actual, 152)

    def test_sum_check_two_numbers_end_pass(self):
        # Selected numbers are 19 and 9
        input_list = [4, 8, 19, 55, 9]
        actual = main.sum_check(input_list, 28, 2, [])
        self.assertEqual(actual, 171)

    def test_sum_check_three_numbers_start_pass(self):
        # Selected numbers are 4, 8 and 55
        input_list = [4, 8, 19, 55, 9]
        actual = main.sum_check(input_list, 67, 3, [])
        self.assertEqual(actual, 1760)

    def test_sum_check_three_numbers_middle_pass(self):
        # Selected numbers are 8, 19 and 55
        input_list = [4, 8, 19, 55, 9]
        actual = main.sum_check(input_list, 82, 3, [])
        self.assertEqual(actual, 8360)

    def test_sum_check_three_numbers_end_pass(self):
        # Selected numbers are 8, 19 and 9
        input_list = [4, 8, 19, 55, 9]
        actual = main.sum_check(input_list, 36, 3, [])
        self.assertEqual(actual, 1368)


if __name__ == '__main__':
    unittest.main()
