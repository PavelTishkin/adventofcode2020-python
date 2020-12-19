import unittest

from day17 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.init_cubes_str = [".#.", "..#", "###"]

    def test_load_init_cubes_returns_correct_cubes(self):
        actual = main.load_init_cubes(self.init_cubes_str, 3)
        self.assertIn(main.Cube(3, [1, 0, 0]), actual)
        self.assertIn(main.Cube(3, [2, 2, 0]), actual)
        self.assertNotIn(main.Cube(3, [0, 1, 0]), actual)

    def test_cube_is_neighbour_detects_correct_neighbours(self):
        this_cube = main.Cube(3, [0, 0, 0])
        other_cube = main.Cube(3, [-1, -1, -1])
        self.assertTrue(this_cube.is_neighbour(other_cube))
        other_cube = main.Cube(3, [1, 1, 1])
        self.assertTrue(this_cube.is_neighbour(other_cube))
        other_cube = main.Cube(3, [1, 1, 2])
        self.assertFalse(this_cube.is_neighbour(other_cube))

    def test_cycle_cubes_returns_correct_state(self):
        cubes_state = main.load_init_cubes(self.init_cubes_str, 3)
        cubes_state = main.cycle_cubes(cubes_state)
        self.assertIn(main.Cube(3, [0, 1, -1]), cubes_state)
        self.assertIn(main.Cube(3, [1, 3, 0]), cubes_state)
        self.assertNotIn(main.Cube(3, [0, 0, 1]), cubes_state)

    def test_3d_active_count_after_number_of_cycles(self):
        cubes_state = main.load_init_cubes(self.init_cubes_str, 3)
        for _ in range(6):
            cubes_state = main.cycle_cubes(cubes_state)
        self.assertEqual(len(cubes_state), 112)

    def test_4d_active_count_after_number_of_cycles(self):
        cubes_state = main.load_init_cubes(self.init_cubes_str, 4)
        for _ in range(6):
            cubes_state = main.cycle_cubes(cubes_state)
        self.assertEqual(len(cubes_state), 848)
