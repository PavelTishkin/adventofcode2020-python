import unittest

from day3 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.input_data = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ]

    def test_count_trees_path1(self):
        path = [1, 1]
        actual = main.count_trees(self.input_data, path)
        self.assertEqual(actual, 2)

    def test_count_trees_path2(self):
        path = [3, 1]
        actual = main.count_trees(self.input_data, path)
        self.assertEqual(actual, 7)

    def test_count_trees_path3(self):
        path = [5, 1]
        actual = main.count_trees(self.input_data, path)
        self.assertEqual(actual, 3)

    def test_count_trees_path4(self):
        path = [7, 1]
        actual = main.count_trees(self.input_data, path)
        self.assertEqual(actual, 4)

    def test_count_trees_path5(self):
        path = [1, 2]
        actual = main.count_trees(self.input_data, path)
        self.assertEqual(actual, 2)
