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

        is_adjacent, _ = tiles[1951].is_adjacent(tiles[2729])
        self.assertTrue(is_adjacent)
        is_adjacent, _ = tiles[2473].is_adjacent(tiles[1427])
        self.assertTrue(is_adjacent)
        is_adjacent, _ = tiles[2971].is_adjacent(tiles[1427])
        self.assertFalse(is_adjacent)

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

    def test_set_neighbours_flipped_sets_correct_flag(self):
        tiles = main.parse_tiles(self.tiles_txt)
        main.set_adjacent_tiles(tiles)
        corner_tile = tiles[1951]
        corner_tile.set_neighbors_flipped('normal')
        self.assertEqual(corner_tile.is_flipped, 'normal')
        self.assertEqual(tiles[1171].is_flipped, 'normal')
        self.assertEqual(tiles[3079].is_flipped, 'flipped')

    def test_normalize_tiles_return_correct_orientation(self):
        tiles = main.parse_tiles(self.tiles_txt)
        main.set_adjacent_tiles(tiles)
        corner_tile = tiles[1951]
        main.normalize_tiles(corner_tile.tile_id, tiles)
        self.assertEqual(tiles[1171].adjacent_tiles[3].tile_id, 2473)

    def test_compile_tile_array_returns_correct_array(self):
        tiles = main.parse_tiles(self.tiles_txt)
        main.set_adjacent_tiles(tiles)
        main.normalize_tiles(1951, tiles)
        actual = main.compile_tile_array(1951, tiles)
        self.assertEqual(len(actual), 3)
        self.assertEqual(len(actual[0]), 3)
        self.assertEqual(actual[0][0].tile_id, 1951)
        self.assertEqual(actual[0][1].tile_id, 2729)
        self.assertEqual(actual[0][2].tile_id, 2971)
        self.assertEqual(actual[1][0].tile_id, 2311)
        self.assertEqual(actual[1][1].tile_id, 1427)
        self.assertEqual(actual[1][2].tile_id, 1489)
        self.assertEqual(actual[2][0].tile_id, 3079)
        self.assertEqual(actual[2][1].tile_id, 2473)
        self.assertEqual(actual[2][2].tile_id, 1171)

    def test_flipped_edge_same_as_transformed(self):
        tile = main.parse_tiles(self.tiles_txt)[1951]
        flipped_data = main.transform_2d_array(tile.tile_cells, 0, True)
        self.assertEqual(tile.flipped_edges[0], ''.join(flipped_data[0]))

    def test_get_whole_picture_returns_correct_data(self):
        tiles = main.parse_tiles(self.tiles_txt)
        main.set_adjacent_tiles(tiles)
        main.normalize_tiles(1951, tiles)
        tile_array = main.compile_tile_array(1951, tiles)

        actual = main.get_whole_picture(tile_array)
        actual = main.transform_2d_array(actual, 3, True)

        self.assertEqual(''.join(actual[0]), '.#.#..#.##...#.##..#####')
        self.assertEqual(''.join(actual[len(actual)-1]), '...###...##...#...#..###')

    def test_is_pattern_present_finds_valid_pattern(self):
        image = ['.##.#',
                 '#.###']
        pattern = [' #  #',
                   '# # #']
        self.assertTrue(main.is_pattern_present(image, pattern))

    def test_is_pattern_present_finds_invalid_pattern(self):
        image = ['.##..',
                 '#.###']
        pattern = [' #  #',
                   '# # #']
        self.assertFalse(main.is_pattern_present(image, pattern))

    def test_get_pattern_count_returns_correct_count(self):
        image = ['.##..',
                 '#.##.',
                 '#.#.#']
        pattern = [' # ',
                   '# #']
        self.assertEqual(main.get_pattern_count(image, pattern), 2)

    def test_get_nessie_count_returns_correct_count(self):
        tiles = main.parse_tiles(self.tiles_txt)
        main.set_adjacent_tiles(tiles)
        main.normalize_tiles(1951, tiles)
        tile_array = main.compile_tile_array(1951, tiles)

        image = main.get_whole_picture(tile_array)
        actual = main.get_nessie_count(image, main.sea_monster)
        self.assertEqual(actual, 2)
