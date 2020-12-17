def main():
    input_file = open('input/day17.txt', 'r')
    init_cubes_str = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    cubes_state = load_init_cubes(init_cubes_str)
    for _ in range(6):
        cubes_state = cycle_cubes(cubes_state)
    print('Answer 1: {}'.format(len(cubes_state)))


def load_init_cubes(init_cubes_str):
    cubes = []
    for y, row in enumerate(init_cubes_str):
        for x, state in enumerate(row):
            if state == '#':
                cubes.append(Cube(x, y, 0))
    return cubes


def cycle_cubes(cubes_state):
    new_cubes_state = []
    all_cube_neighbours = set()
    for cube in cubes_state:
        all_cube_neighbours.update(cube.get_all_neighbours())
        if len(cube.get_active_neighbours(cubes_state)) in (2, 3):
            new_cubes_state.append(cube)
    for cube in all_cube_neighbours:
        if cube not in cubes_state and len(cube.get_active_neighbours(cubes_state)) == 3:
            new_cubes_state.append(cube)

    return new_cubes_state


class Cube:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def get_all_neighbours(self):
        neighbour_cubes = []
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                for z in range(self.z - 1, self.z + 2):
                    new_cube = Cube(x, y, z)
                    if new_cube != self:
                        neighbour_cubes.append(new_cube)
        return neighbour_cubes

    def get_active_neighbours(self, cells_state):
        all_neighbours = self.get_all_neighbours()
        return [c for c in all_neighbours if c in cells_state]

    def get_inactive_neighbours(self, cells_state):
        all_neighbours = self.get_all_neighbours()
        return [c for c in all_neighbours if c not in cells_state]

    def is_neighbour(self, other):
        return self != other and \
               abs(self.x - other.x) <= 1 and \
               abs(self.y - other.y) <= 1 and \
               abs(self.z - other.z) <= 1

    def __repr__(self):
        return f'({self.x}; {self.y}; {self.z})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))


def print_cubes_state(cubes_state):
    min_x, min_y, min_z = cubes_state[0].x, cubes_state[0].y, cubes_state[0].z
    max_x, max_y, max_z = min_x, min_y, min_z

    for cube in cubes_state:
        min_x = cube.x if cube.x < min_x else min_x
        min_y = cube.y if cube.y < min_y else min_y
        min_z = cube.z if cube.z < min_z else min_z
        max_x = cube.x if cube.x > max_x else max_x
        max_y = cube.y if cube.y > max_y else max_y
        max_z = cube.z if cube.z > max_z else max_z

    for z in range(min_z, max_z+1):
        print(f'z={z}')
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if Cube(x, y, z) in cubes_state:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
        print('')


if __name__ == '__main__':
    main()
