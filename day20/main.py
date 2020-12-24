import re

rotation_matrix = [
    [0, 3, 2, 1],
    [1, 0, 3, 2],
    [2, 1, 0, 3],
    [3, 2, 1, 0]
]

sea_monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]


def main():
    input_file = open('input/day20.txt', 'r')
    tiles_txt = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    corners_product = 1
    corner_tile_id = 0
    tiles = parse_tiles(tiles_txt)
    for tile in tiles.values():
        tile.set_adjacent_tiles(tiles.values())
        if len(tile.adjacent_tiles) == 2:
            corner_tile_id = tile.tile_id
            corners_product *= tile.tile_id

    print('Answer 1: {}'.format(corners_product))

    normalize_tiles(corner_tile_id, tiles)
    tile_array = compile_tile_array(corner_tile_id, tiles)

    image = get_whole_picture(tile_array)
    nessie_count = get_nessie_count(image, sea_monster)
    pixels_count = count_chars(image, '#')
    nessie_pixels_count = count_chars(sea_monster, '#')

    print('Answer 2: {}'.format(pixels_count - nessie_pixels_count * nessie_count))


def parse_tiles(tiles_txt):
    """
    Parse text data containing list of tiles
    :param tiles_txt: Text data
    :return: Set of tiles using tile id as a key
    """
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


def transform_2d_array(original, rotate=0, flip=False):
    """
    Transforms a 2d array through rotation and mirror flip
    :param original: Original array to transform
    :param rotate: Number of times to rotate original array clockwise 90 degrees
    :param flip: True to mirror flip array
    :return: Transformed array
    """
    transformed = original
    for i in range(rotate):
        transformed = [list(r) for r in zip(*transformed[::-1])]
    if flip:
        transformed = transformed[:]
        transformed.reverse()

    return transformed


def normalize_tiles(corner_tile_id, all_tiles):
    """
    Rotates and flips tiles, using a selected corner tile as a starting point until all tiles are oriented 
    and flipped in the same direction
    """
    corner_tile = all_tiles[corner_tile_id]
    corner_tile.set_neighbors_flipped('normal')
    for tile in all_tiles.values():
        if tile.is_flipped == 'flipped':
            tile.is_flipped = 'normal'
            flipped_data = transform_2d_array(tile.tile_cells, 0, True)
            tile.tile_cells = flipped_data
            tile.load_edges()
    set_adjacent_tiles(all_tiles)
    corner_tile = all_tiles[corner_tile_id]
    rotated_data = transform_2d_array(corner_tile.tile_cells,
                                      (1 - min(corner_tile.adjacent_tiles.keys())) % 4, False)
    all_tiles[corner_tile_id] = Tile(corner_tile_id, rotated_data)
    corner_tile = all_tiles[corner_tile_id]
    corner_tile.is_rotated = True
    set_adjacent_tiles(all_tiles)
    corner_tile.rotate_neighbours(all_tiles)


def compile_tile_array(corner_tile_id, all_tiles):
    tiles_array = []

    next_edge_tile = all_tiles[corner_tile_id]
    while True:
        next_tile = next_edge_tile
        tiles_row = [next_tile]
        while 1 in next_tile.adjacent_tiles:
            next_tile = next_tile.adjacent_tiles[1]
            tiles_row.append(next_tile)
        tiles_array.append(tiles_row)

        if 2 in next_edge_tile.adjacent_tiles:
            next_edge_tile = next_edge_tile.adjacent_tiles[2]
        else:
            break

    return tiles_array


def get_whole_picture(tiles_array):
    whole_picture = []
    for row in tiles_array:
        row_data = [row_item.get_cut_tile_data() for row_item in row]
        whole_picture.extend(list(''.join(line)) for line in zip(*row_data))
    return whole_picture


def get_nessie_count(image, pattern):
    for rotate in range(4):
        for flip in [True, False]:
            new_image = transform_2d_array(image, rotate, flip)
            pattern_count = get_pattern_count(new_image, pattern)
            if pattern_count > 0:
                return pattern_count


def get_pattern_count(image, pattern):
    pattern_count = 0
    for y in range(0, len(image) - len(pattern) + 1):
        for x in range(0, len(image[y]) - len(pattern[0]) + 1):
            sub_image = []
            for sub_y in range(len(pattern)):
                sub_image.append(image[y + sub_y][x:x + len(pattern[sub_y])])
            if is_pattern_present(sub_image, pattern):
                pattern_count += 1
    return pattern_count


def is_pattern_present(image, pattern):
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            if pattern[y][x] != ' ' and pattern[y][x] != image[y][x]:
                return False
    return True


def count_chars(image, char):
    char_count = 0
    for row in image:
        for c in row:
            if c == char:
                char_count += 1
    return char_count


class Tile:

    def __init__(self, tile_id, tile_data):
        self.tile_id = tile_id
        self.tile_data = tile_data
        self.tile_cells = [[]]
        self.edge_length = 0
        self.load_tile_data()
        self.edges = {}
        self.flipped_edges = {}
        self.load_edges()
        self.neighbours = set()
        self.flipped_neighbours = set()
        self.adjacent_tiles = {}
        self.is_flipped = 'none'
        self.is_rotated = False

    def load_tile_data(self):
        """
        Initialize tile with data and set edge length
        """
        self.tile_cells = []
        for tile_line in self.tile_data:
            self.tile_cells.append([c for c in tile_line])
        self.edge_length = len(self.tile_data[0])

    def load_edges(self):
        """
        Initialize list of edges and flipped edges. Edges are indexed 0-4 starting from top and going clockwise
        """
        self.edges = {}
        self.flipped_edges = {}
        flipped_cells = transform_2d_array(self.tile_cells, 0, True)
        # Top edge
        self.edges[0] = ''.join(self.tile_cells[0])
        self.flipped_edges[0] = ''.join(flipped_cells[0])
        # Right edge
        self.edges[1] = ''.join([line[self.edge_length-1] for line in self.tile_cells])
        self.flipped_edges[1] = ''.join([line[self.edge_length-1] for line in flipped_cells])
        # Bottom edge
        self.edges[2] = ''.join(self.tile_cells[self.edge_length - 1])[::-1]
        self.flipped_edges[2] = ''.join(flipped_cells[self.edge_length - 1])[::-1]
        # Left edge
        self.edges[3] = ''.join([line[0] for line in self.tile_cells][::-1])
        self.flipped_edges[3] = ''.join([line[0] for line in flipped_cells][::-1])

    def set_adjacent_tiles(self, other_tiles):
        self.adjacent_tiles = {}
        self.neighbours = set()
        self.flipped_neighbours = set()
        for other_tile in other_tiles:
            is_adjacent, edge_id = self.is_adjacent(other_tile)
            if is_adjacent:
                self.adjacent_tiles[edge_id] = other_tile

    def is_adjacent(self, other):
        if self == other:
            return False, 0
        for edge_id, edge in self.edges.items():
            if edge in other.edges.values():
                self.flipped_neighbours.add(other)
                return True, edge_id
            elif edge in other.flipped_edges.values():
                self.neighbours.add(other)
                return True, edge_id
        return False, 0

    def set_neighbors_flipped(self, is_current_flipped):
        if self.is_flipped != 'none':
            return
        self.is_flipped = is_current_flipped
        for neighbour in self.neighbours:
            neighbour.set_neighbors_flipped(self.is_flipped)
        for neighbour in self.flipped_neighbours:
            if self.is_flipped == 'normal':
                neighbour.set_neighbors_flipped('flipped')
            elif self.is_flipped == 'flipped':
                neighbour.set_neighbors_flipped('normal')

    def rotate_neighbours(self, all_tiles):
        for direction, neighbour in self.adjacent_tiles.items():
            if not neighbour.is_rotated:
                neighbour.rotate_to_match(self, direction, all_tiles)

    def rotate_to_match(self, other_tile, other_tile_direction, all_tiles):
        """
        Will rotate current tile to align directions of the edges relative to a neighbour tile
        """
        self.is_rotated = True
        for my_direction, tile in self.adjacent_tiles.items():
            if tile.tile_id == other_tile.tile_id:
                direction_required = (other_tile_direction - 2) % 4
                rotate_angle = rotation_matrix[direction_required][my_direction]
                if rotate_angle != 0:
                    self.tile_cells = transform_2d_array(self.tile_cells, rotate_angle, False)
                    self.load_edges()
                    self.set_adjacent_tiles(all_tiles.values())
        self.rotate_neighbours(all_tiles)

    def get_cut_tile_data(self):
        cut_tile_data = []
        for i in range(1, len(self.tile_cells)-1):
            cut_tile_data.append(''.join(self.tile_cells[i][1:-1]))
        return cut_tile_data

    def __eq__(self, other):
        return self.tile_id == other.tile_id

    def __hash__(self):
        return hash(self.tile_id)

    def __repr__(self):
        return f'id:{self.tile_id}'


if __name__ == '__main__':
    main()
