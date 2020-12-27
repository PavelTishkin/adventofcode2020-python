import unittest

from day24 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.tiles_directions_txt = [
            'sesenwnenenewseeswwswswwnenewsewsw',
            'neeenesenwnwwswnenewnwwsewnenwseswesw',
            'seswneswswsenwwnwse',
            'nwnwneseeswswnenewneswwnewseswneseene',
            'swweswneswnenwsewnwneneseenw',
            'eesenwseswswnenwswnwnwsewwnwsene',
            'sewnenenenesenwsewnenwwwse',
            'wenwwweseeeweswwwnwwe',
            'wsweesenenewnwwnwsenewsenwwsesesenwne',
            'neeswseenwwswnwswswnw',
            'nenwswwsewswnenenewsenwsenwnesesenew',
            'enewnwewneswsewnwswenweswnenwsenwsw',
            'sweneswneswneneenwnewenewwneswswnese',
            'swwesenesewenwneswnwwneseswwne',
            'enesenwswwswneneswsenwnewswseenwsese',
            'wnwnesenesenenwwnenwsewesewsesesew',
            'nenewswnwewswnenesenwnesewesw',
            'eneswnwswnwsenenwnwnwwseeswneewsenese',
            'neswnwewnwnwseenwseesewsenwsweewe',
            'wseweeenwnesenwwwswnew'
        ]

    def test_split_directions_returns_correct_directions(self):
        actual = main.split_directions('seswneswswsenwwnwse')
        self.assertEqual(actual, ['se', 'sw', 'ne', 'sw', 'sw', 'se', 'nw', 'w', 'nw', 'se'])

    def test_load_directions_returns_correct_directions(self):
        actual = main.load_directions_list(self.tiles_directions_txt)
        self.assertEqual(actual[2], ['se', 'sw', 'ne', 'sw', 'sw', 'se', 'nw', 'w', 'nw', 'se'])

    def test_load_hex_tiles_flips_color_tiles(self):
        directions_list = main.load_directions_list(self.tiles_directions_txt)
        hex_tiles = main.load_hex_tiles(directions_list)
        self.assertEqual(len(hex_tiles), 15)
        self.assertEqual(len(main.get_tiles_by_color(hex_tiles, 'black')), 10)
        self.assertEqual(len(main.get_tiles_by_color(hex_tiles, 'white')), 5)

    def test_advance_day_returns_correct_tile_count(self):
        directions_list = main.load_directions_list(self.tiles_directions_txt)
        hex_tiles = main.load_hex_tiles(directions_list)
        actual = main.advance_day(hex_tiles)
        self.assertEqual(len(main.get_tiles_by_color(actual, 'black')), 15)

    def test_advance_multiple_days_returns_correct_tile_count(self):
        directions_list = main.load_directions_list(self.tiles_directions_txt)
        hex_tiles = main.load_hex_tiles(directions_list)
        for i in range(100):
            hex_tiles = main.advance_day(hex_tiles)
        self.assertEqual(len(main.get_tiles_by_color(hex_tiles, 'black')), 2208)
