def main():
    input_file = open('input/day17.txt', 'r')
    init_cubes_str = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    cubes_state = load_init_cubes(init_cubes_str, 3)
    for _ in range(6):
        cubes_state = cycle_cubes(cubes_state)
    print('Answer 1: {}'.format(len(cubes_state)))

    cubes_state = load_init_cubes(init_cubes_str, 4)
    for _ in range(6):
        cubes_state = cycle_cubes(cubes_state)
    print('Answer 2: {}'.format(len(cubes_state)))


def load_init_cubes(init_cubes_str, dimension_count):
    cubes = []
    for y, row in enumerate(init_cubes_str):
        for x, state in enumerate(row):
            if state == '#':
                dimensions = [x, y] + [0]*(dimension_count - 2)
                cubes.append(Cube(dimension_count, dimensions))
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

    def __init__(self, dimension_count=3, values=[]):
        self.dimension_count = dimension_count
        self.dimensions = []
        for i in range(self.dimension_count):
            self.dimensions.append(values[i])

    def get_all_neighbours(self, prev_dimensions=[]):
        neighbours = []
        curr_dim_value = self.dimensions[len(prev_dimensions)]
        for d in range(curr_dim_value - 1, curr_dim_value + 2):
            curr_dimensions = prev_dimensions[:] + [d]
            if len(curr_dimensions) == self.dimension_count:
                new_cube = Cube(self.dimension_count, curr_dimensions)
                if new_cube != self:
                    neighbours.append(new_cube)
            else:
                neighbours.extend(self.get_all_neighbours(curr_dimensions))
        return neighbours

    def get_active_neighbours(self, cells_state):
        all_neighbours = list(self.get_all_neighbours())
        return [c for c in all_neighbours if c in cells_state]

    def get_inactive_neighbours(self, cells_state):
        all_neighbours = list(self.get_all_neighbours())
        return [c for c in all_neighbours if c not in cells_state]

    def is_neighbour(self, other):
        for i in range(self.dimension_count):
            if abs(other.dimensions[i] + self.dimensions[i]) > 1:
                return False
        return True

    def __repr__(self):
        return f'({"; ".join(str(d) for d in self.dimensions)})'

    def __eq__(self, other):
        if self.dimension_count != other.dimension_count:
            return False
        for i in range(self.dimension_count):
            if self.dimensions[i] != other.dimensions[i]:
                return False
        return True

    def __hash__(self):
        return hash(tuple(self.dimensions))


if __name__ == '__main__':
    main()
