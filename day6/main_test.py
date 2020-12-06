import unittest

from day6 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.input_data = [
            "abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b"
        ]

    def test_parse_groups_everyone_returns_correct_data(self):
        actual = main.parse_groups(self.input_data, False)
        print(actual)
        self.assertEqual(len(actual[0]), 3)
        self.assertEqual(len(actual[1]), 3)
        self.assertEqual(len(actual[2]), 3)
        self.assertEqual(len(actual[3]), 1)
        self.assertEqual(len(actual[4]), 1)

    def test_parse_groups_anyone_returns_correct_data(self):
        actual = main.parse_groups(self.input_data, True)
        print(actual)
        self.assertEqual(len(actual[0]), 3)
        self.assertEqual(len(actual[1]), 0)
        self.assertEqual(len(actual[2]), 1)
        self.assertEqual(len(actual[3]), 1)
        self.assertEqual(len(actual[4]), 1)
