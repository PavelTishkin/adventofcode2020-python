import unittest

from day2 import main


class MainTestCase(unittest.TestCase):

    def test_check_pass_type1_example1(self):
        actual = main.check_password("1-3 a: abcde", 1)
        self.assertTrue(actual)

    def test_check_pass_type1_example2(self):
        actual = main.check_password("1-3 b: cdefg", 1)
        self.assertFalse(actual)

    def test_check_pass_type1_example3(self):
        actual = main.check_password("2-9 c: ccccccccc", 1)
        self.assertTrue(actual)

    def test_check_pass_type2_example1(self):
        actual = main.check_password("1-3 a: abcde", 2)
        self.assertTrue(actual)

    def test_check_pass_type2_example2(self):
        actual = main.check_password("1-3 b: cdefg", 2)
        self.assertFalse(actual)

    def test_check_pass_type2_example3(self):
        actual = main.check_password("2-9 c: ccccccccc", 2)
        self.assertFalse(actual)
