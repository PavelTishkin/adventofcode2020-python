import re


def main():
    input_file = open('input/day20.txt', 'r')
    tiles_txt = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    corners_product = 1
    tiles = parse_tiles(tiles_txt)
    for tile in tiles.values():
        tile.set_adjacent_tiles(tiles.values())
        if len(tile.adjacent_tiles) == 2:
            corners_product *= tile.tile_id

    print('Answer 1: {}'.format(corners_product))


def parse_tiles(tiles_txt):
    tiles = {}

    tile_id = 0
    tile_data = []
    for tile_line in tiles_txt:
        if tile_line == '':
            if tile_data:
                new_tile = Tile(tile_id, tile_data)
                tiles[tile_id] = new_tile
            tile_id = 0
            tile_data = []
            None
        elif tile_line.startswith('Tile'):
            r = re.match(r'Tile (\d*):', tile_line)
            tile_id = int(r.group(1))
        else:
            tile_data.append(tile_line)

    return tiles


def set_adjacent_tiles(tiles):
    for tile in tiles.values():
        tile.set_adjacent_tiles(tiles.values())


class Tile:

    def __init__(self, tile_id, tile_data):
        self.tile_id = tile_id
        self.tile_data = tile_data
        self.tile_cells = [[]]
        self.edge_length = 0
        self.load_tile_data()
        self.edges = []
        self.flipped_edges = []
        self.load_edges()
        self.neighbours = set()
        self.flipped_neighbours = set()
        self.adjacent_tiles = []

    def load_tile_data(self):
        self.tile_cells = []
        for tile_line in self.tile_data:
            self.tile_cells.append([c for c in tile_line])
        self.edge_length = len(self.tile_data[0])

    def load_edges(self):
        self.edges = []
        self.flipped_edges = []
        # Top edge
        self.edges.append(''.join(self.tile_cells[0]))
        # Right edge
        self.edges.append(''.join([line[self.edge_length-1] for line in self.tile_cells]))
        # Bottom edge
        self.edges.append(''.join(self.tile_cells[self.edge_length - 1])[::-1])
        # Left edge
        self.edges.append(''.join([line[0] for line in self.tile_cells][::-1]))
        for edge in self.edges:
            self.flipped_edges.append(edge[::-1])

    def set_adjacent_tiles(self, other_tiles):
        self.adjacent_tiles = []
        for other_tile in other_tiles:
            if self.is_adjacent(other_tile):
                self.adjacent_tiles.append(other_tile)

    def is_adjacent(self, other):
        if self == other:
            return False
        for edge in self.edges:
            if edge in other.edges:
                self.neighbours.add(other)
                return True
            elif edge in other.flipped_edges:
                self.flipped_neighbours.add(other)
                return True
        return False

    def __eq__(self, other):
        return self.tile_id == other.tile_id

    def __hash__(self):
        return hash(self.tile_id)

    def __repr__(self):
        return f'id:{self.tile_id}'


if __name__ == '__main__':
    main()
