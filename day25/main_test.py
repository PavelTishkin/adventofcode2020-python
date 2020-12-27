import unittest

from day25 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.card_pub_key = 5764801
        self.door_pub_key = 17807724

    def test_transform_returns_correct_number(self):
        actual = main.transform(8, 7)
        self.assertEqual(actual, self.card_pub_key)

    def test_find_loop_returns_correct_loop(self):
        actual = main.find_loop(self.door_pub_key)
        self.assertEqual(actual, 11)

    def test_find_encryption_key_returns_correct_key(self):
        actual = main.find_encryption_key(self.card_pub_key, self.door_pub_key)
        self.assertEqual(actual, 14897079)

    def test_baby_step_giant_step(self):
        actual = main.baby_step_giant_step(7, self.door_pub_key, 20201227)
        self.assertEqual(actual, 11)
