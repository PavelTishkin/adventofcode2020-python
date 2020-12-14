import unittest

from day13 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.current_timestamp = 939
        self.schedule = [7, 13, 0, 0, 59, 0, 31, 19]

    def test_get_get_bus_departure_returns_correct_timestamp(self):
        actual = main.get_bus_departure(self.current_timestamp, self.schedule[1])
        self.assertEqual(actual, 949)

    def test_get_get_bus_departure_returns_correct_timestamp_when_departure_is_now(self):
        actual = main.get_bus_departure(938, self.schedule[0])
        self.assertEqual(actual, 938)

    def test_get_next_departure_returns_correct_bus_timestamps(self):
        actual = main.get_next_departure(self.current_timestamp, self.schedule)
        self.assertEqual(actual[0], 59)
        self.assertEqual(actual[1], 944)

    def test_has_timestamp_sequential_departure_detects_valid_timestamp(self):
        actual = main.has_timestamp_sequential_departure(1068781, self.schedule)
        self.assertTrue(actual)

    def test_has_timestamp_sequential_departure_detects_invalid_timestamp(self):
        actual = main.has_timestamp_sequential_departure(1068782, self.schedule)
        self.assertFalse(actual)

    def test_get_first_timestamp_sequential_departure_schedule1(self):
        schedule = [17, 0, 13, 19]
        actual = main.get_first_timestamp_sequential_departure(schedule)
        self.assertEqual(actual, 3417)

    def test_get_first_timestamp_sequential_departure_schedule2(self):
        schedule = [67, 7, 59, 61]
        actual = main.get_first_timestamp_sequential_departure(schedule)
        self.assertEqual(actual, 754018)

    def test_get_first_timestamp_sequential_departure_schedule3(self):
        schedule = [67, 0, 7, 59, 61]
        actual = main.get_first_timestamp_sequential_departure(schedule)
        self.assertEqual(actual, 779210)

    def test_get_first_timestamp_sequential_departure_schedule4(self):
        schedule = [67, 7, 0, 59, 61]
        actual = main.get_first_timestamp_sequential_departure(schedule)
        self.assertEqual(actual, 1261476)

    def test_get_first_timestamp_sequential_departure_schedule5(self):
        schedule = [1789, 37, 47, 1889]
        actual = main.get_first_timestamp_sequential_departure(schedule)
        self.assertEqual(actual, 1202161486)
