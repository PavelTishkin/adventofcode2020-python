import unittest

from day16 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.ticket_lines = [
            "class: 1-3 or 5-7",
            "row: 6-11 or 33-44",
            "seat: 13-40 or 45-50",
            "",
            "your ticket:",
            "7,1,14",
            "",
            "nearby tickets:",
            "7,3,47",
            "40,4,50",
            "55,2,20",
            "38,6,12"
        ]

    def test_load_ticket_data_returns_correct_data(self):
        actual = main.load_tickets_data(self.ticket_lines)
        self.assertIn(1, actual['rules']['class'])
        self.assertIn(7, actual['rules']['row'])
        self.assertNotIn(4, actual['rules']['seat'])
        self.assertEqual(actual['my_ticket'], [7, 1, 14])
        self.assertIn([7, 3, 47], actual['near_tickets'])

    def test_get_invalid_fields_validates_correct_ticket(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        actual = main.get_invalid_fields(tickets_data['rules'], tickets_data['near_tickets'][0])
        self.assertEqual(actual, [])

    def test_get_invalid_fields_validates_incorrect_ticket1(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        actual = main.get_invalid_fields(tickets_data['rules'], tickets_data['near_tickets'][1])
        self.assertEqual(actual, [4])

    def test_get_invalid_fields_validates_incorrect_ticket2(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        actual = main.get_invalid_fields(tickets_data['rules'], tickets_data['near_tickets'][2])
        self.assertEqual(actual, [55])

    def test_get_invalid_fields_validates_incorrect_ticket3(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        actual = main.get_invalid_fields(tickets_data['rules'], tickets_data['near_tickets'][3])
        self.assertEqual(actual, [12])

    def test_get_tickets_error_rate_returns_correct_count(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        actual = main.get_tickets_error_rate(tickets_data)
        self.assertEqual(actual, 71)

    def test_get_valid_tickets_returns_correct_tickets(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        actual = main.get_valid_tickets(tickets_data)
        self.assertEqual(actual, [[7, 3, 47]])

    def test_is_valid_order_validates_correct_order(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        valid_tickets = main.get_valid_tickets(tickets_data)
        guess_order = ['row', 'class', 'seat']
        actual = main.is_valid_order(guess_order, tickets_data['rules'], valid_tickets)
        self.assertTrue(actual)

    def test_is_valid_order_fails_wrong_order(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        valid_tickets = main.get_valid_tickets(tickets_data)
        guess_order = ['class', 'row', 'seat']
        actual = main.is_valid_order(guess_order, tickets_data['rules'], valid_tickets)
        self.assertFalse(actual)

    def test_guess_order_returns_correct_order(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        valid_tickets = main.get_valid_tickets(tickets_data)
        fields = list(tickets_data['rules'].keys())
        actual = main.guess_order([], fields, tickets_data['rules'], valid_tickets)
        self.assertEqual(actual, ['row', 'class', 'seat'])

    def test_get_ticket_field_by_name_returns_correct_field(self):
        tickets_data = main.load_tickets_data(self.ticket_lines)
        order = ['row', 'class', 'seat']
        actual = main.get_ticket_field_by_name(tickets_data['my_ticket'], 'class', order)
        self.assertEqual(actual, 1)
