import unittest

from day5 import main


class MainTestCase(unittest.TestCase):

    def test_get_ticket_data_returns_correct_data(self):
        actual = main.get_ticket_data('FBFBBFFRLR')
        self.assertEqual(actual['row'], 44)
        self.assertEqual(actual['col'], 5)
        self.assertEqual(actual['id'], 357)

        actual = main.get_ticket_data('BFFFBBFRRR')
        self.assertEqual(actual['row'], 70)
        self.assertEqual(actual['col'], 7)
        self.assertEqual(actual['id'], 567)

        actual = main.get_ticket_data('FFFBBBFRRR')
        self.assertEqual(actual['row'], 14)
        self.assertEqual(actual['col'], 7)
        self.assertEqual(actual['id'], 119)

        actual = main.get_ticket_data('BBFFBBFRLL')
        self.assertEqual(actual['row'], 102)
        self.assertEqual(actual['col'], 4)
        self.assertEqual(actual['id'], 820)
