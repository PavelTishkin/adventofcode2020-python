def main():
    input_file = open('input/day24.txt', 'r')
    tiles_directions_txt = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    directions_list = load_directions_list(tiles_directions_txt)
    hex_tiles = load_hex_tiles(directions_list)
    print('Answer 1: {}'.format(len(get_tiles_by_color(hex_tiles, 'black'))))

    for i in range(100):
        hex_tiles = advance_day(hex_tiles)
    print('Answer 2: {}'.format(len(get_tiles_by_color(hex_tiles, 'black'))))


def load_hex_tiles(directions_list):
    hex_tiles = []
    for directions in directions_list:
        hex_tile = HexTile()
        hex_tile.move_directions(directions)
        hex_tile.flip_color()
        if hex_tile in hex_tiles:
            hex_tiles[hex_tiles.index(hex_tile)].flip_color()
        else:
            hex_tiles.append(hex_tile)
    return set(hex_tiles)


def advance_day(hex_tiles):
    new_hex_tiles = set()
    all_hex_tiles = get_all_neighbours(hex_tiles)
    for hex_tile in all_hex_tiles:
        black_neighbours_count = len(get_tiles_by_color(hex_tile.get_matching_neighbours(hex_tiles), 'black'))
        if hex_tile.color == 'black':
            if black_neighbours_count in [1, 2]:
                new_hex_tiles.add(hex_tile)
        else:
            if black_neighbours_count == 2:
                new_hex_tile = HexTile(hex_tile.x, hex_tile.y, hex_tile.z)
                new_hex_tile.color = 'black'
                new_hex_tiles.add(new_hex_tile)
    return new_hex_tiles


def get_all_neighbours(hex_tiles):
    neighbour_tiles = set()
    for hex_tile in hex_tiles:
        neighbour_tiles.update(set(hex_tile.get_neighbours()) - hex_tiles)
    neighbour_tiles.update(hex_tiles)
    return neighbour_tiles


def get_tiles_by_color(hex_tiles, color):
    return [hex_tile for hex_tile in hex_tiles if hex_tile.color == color]


def load_directions_list(directions_txt):
    return [split_directions(directions_str) for directions_str in directions_txt]


def split_directions(directions_str):
    directions_list = []
    while len(directions_str) > 0:
        if directions_str.startswith('e'):
            directions_list.append('e')
            directions_str = directions_str[1:]
        elif directions_str.startswith('se'):
            directions_list.append('se')
            directions_str = directions_str[2:]
        elif directions_str.startswith('sw'):
            directions_list.append('sw')
            directions_str = directions_str[2:]
        elif directions_str.startswith('w'):
            directions_list.append('w')
            directions_str = directions_str[1:]
        elif directions_str.startswith('nw'):
            directions_list.append('nw')
            directions_str = directions_str[2:]
        elif directions_str.startswith('ne'):
            directions_list.append('ne')
            directions_str = directions_str[2:]
    return directions_list


class HexTile:
    """
    Hex tile is located in a grid by cube coordinates system
    """
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.color = 'white'

    def flip_color(self):
        if self.color == 'black':
            self.color = 'white'
        else:
            self.color = 'black'

    def move_directions(self, directions):
        for direction in directions:
            if direction == 'e':
                self.x += 1
                self.y -= 1
            elif direction == 'se':
                self.y -= 1
                self.z += 1
            elif direction == 'sw':
                self.x -= 1
                self.z += 1
            elif direction == 'w':
                self.x -= 1
                self.y += 1
            elif direction == 'nw':
                self.y += 1
                self.z -= 1
            elif direction == 'ne':
                self.x += 1
                self.z -= 1

    def is_neighbour(self, other):
        return other in self.get_neighbours()

    def get_neighbours(self):
        return [HexTile(self.x + 1, self.y, self.z - 1), HexTile(self.x + 1, self.y - 1, self.z),
                HexTile(self.x, self.y - 1, self.z + 1), HexTile(self.x - 1, self.y, self.z + 1),
                HexTile(self.x - 1, self.y + 1, self.z), HexTile(self.x, self.y + 1, self.z - 1)]

    def get_matching_neighbours(self, hex_tiles):
        matching_neighbours = []
        for hex_tile in hex_tiles:
            if hex_tile.is_neighbour(self):
                matching_neighbours.append(hex_tile)
        return matching_neighbours

    def get_missing_neighbours(self, hex_tiles):
        return list(set(self.get_neighbours()) - set(hex_tiles))

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z}: {self.color})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash(tuple([self.x, self.y, self.z]))


if __name__ == '__main__':
    main()
