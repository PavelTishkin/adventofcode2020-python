import unittest

from day11 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        input_file = open('input/day11_test.txt', 'r')
        self.seats = list(map(lambda l: list(l.strip()), input_file.readlines()))
        input_file.close()

    def test_cycle_seats_single_iteration_returns_correct_seats(self):
        seats, is_flip = main.cycle_seats(self.seats)
        self.assertTrue(is_flip)
        self.assertEqual(seats[0][0], '#')
        self.assertEqual(seats[9][9], '#')

    def test_is_occupied_direction_detects_occupied_seats(self):
        input_data = ['.............',
                      '.L.L.#.#.#.#.',
                      '.............']
        seats = list(map(lambda l: list(l.strip()), input_data))
        actual = main.is_occupied_direction(1, 1, 1, 0, seats)
        self.assertFalse(actual)
        actual = main.is_occupied_direction(3, 1, 1, 0, seats)
        self.assertTrue(actual)

    def test_get_occupied_far_seats_detects_all_occupied_seats(self):
        input_data = ['.......#.',
                      '...#.....',
                      '.#.......',
                      '.........',
                      '..#L....#',
                      '....#....',
                      '.........',
                      '#........',
                      '...#.....']
        seats = list(map(lambda l: list(l.strip()), input_data))
        actual = main.get_occupied_far_seats(3, 4, seats)
        self.assertEqual(actual, 8)

    def test_get_occupied_far_seats_detects_no_occupied_seats(self):
        input_data = ['.##.##.',
                      '#.#.#.#',
                      '##...##',
                      '...L...',
                      '##...##',
                      '#.#.#.#',
                      '.##.##.']
        seats = list(map(lambda l: list(l.strip()), input_data))
        actual = main.get_occupied_far_seats(3, 3, seats)
        self.assertEqual(actual, 0)

    def test_cycle_seats_multiple_iteration_stops_and_has_correct_occupied_count(self):
        seats, is_flip = main.cycle_seats(self.seats)
        round_count = 1
        while is_flip:
            seats, is_flip = main.cycle_seats(seats)
            round_count += 1
        occupied_seats = main.count_occupied_seats(seats)
        self.assertEqual(round_count, 6)
        self.assertEqual(occupied_seats, 37)

    def test_cycle_far_seats_multiple_iteration_stops_and_has_correct_occupied_count(self):
        seats, is_flip = main.cycle_seats(self.seats, True)
        main.print_seats(seats)
        round_count = 1
        while is_flip:
            seats, is_flip = main.cycle_seats(seats, True)
            main.print_seats(seats)
            round_count += 1
        occupied_seats = main.count_occupied_seats(seats)
        self.assertEqual(round_count, 7)
        self.assertEqual(occupied_seats, 26)
