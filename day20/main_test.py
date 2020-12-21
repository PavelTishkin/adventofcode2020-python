import unittest

from day20 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        input_file = open('input/day20_test.txt', 'r')
        self.tiles_txt = list(map(lambda l: l.strip(), input_file.readlines()))
        input_file.close()

    def test_parse_tiles_creates_correct_tiles(self):
        actual = main.parse_tiles(self.tiles_txt)[3079]
        self.assertEqual(actual.tile_id, 3079)
        self.assertIn('..#.###...', actual.tile_data)

    def test_load_tile_data_parses_data_correctly(self):
        actual = main.parse_tiles(self.tiles_txt)[2311]
        self.assertEqual(actual.tile_cells[0][0], '.')
        self.assertEqual(actual.tile_cells[9][9], '#')

    def test_load_edges_parses_edges_correctly(self):
        actual = main.parse_tiles(self.tiles_txt)[2311]
        self.assertEqual(actual.edges[0], '..##.#..#.')
        self.assertEqual(actual.edges[1], '...#.##..#')
        self.assertEqual(actual.edges[2], '###..###..')
        self.assertEqual(actual.edges[3], '.#..#####.')

    def test_is_adjacent_detects_adjacent_pair(self):
        tiles = main.parse_tiles(self.tiles_txt)
        self.assertTrue(tiles[1951].is_adjacent(tiles[2729]))
        self.assertTrue(tiles[2473].is_adjacent(tiles[1427]))
        self.assertFalse(tiles[2971].is_adjacent(tiles[1427]))

    def test_get_adjacent_tiles_returns_correct_count(self):
        tiles = main.parse_tiles(self.tiles_txt)
        main.set_adjacent_tiles(tiles)
        corner_tile_ids = []
        for tile in tiles.values():
            if len(tile.adjacent_tiles) == 2:
                corner_tile_ids.append(tile.tile_id)
        self.assertIn(1951, corner_tile_ids)
        self.assertIn(3079, corner_tile_ids)
        self.assertIn(2971, corner_tile_ids)
        self.assertIn(1171, corner_tile_ids)
        self.assertEqual(len(corner_tile_ids), 4)
