import unittest

from day12 import main
from day12.main import Ship


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.directions = ['F10', 'N3', 'F7', 'R90', 'F11']

    def test_all_instructions_move_to_correct_position(self):
        ship = Ship()
        for instruction in self.directions:
            ship.move(instruction)
        self.assertEqual(ship.x, 17)
        self.assertEqual(ship.y, -8)
        self.assertEqual(ship.get_manhattan_distance(), 25)

    def test_all_instructions_move_with_waypoint_to_correct_position(self):
        ship = Ship()
        for instruction in self.directions:
            ship.move_with_waypoint(instruction)
        self.assertEqual(ship.x, 214)
        self.assertEqual(ship.y, -72)
        self.assertEqual(ship.get_manhattan_distance(), 286)
