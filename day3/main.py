def main():
    input_file = open('input/day3.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))

    path = [3, 1]
    print("Answer 1: {}".format(count_trees(file_lines, path)))

    paths = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    result = 1
    for path in paths:
        result *= count_trees(file_lines, path)
    print("Answer 2: {}".format(result))


def count_trees(input_data, path):
    x, y = path
    tree_count = 0
    while y < len(input_data):
        if input_data[y][x] == '#':
            tree_count += 1
        x = (x + path[0]) % len(input_data[y])
        y += path[1]

    return tree_count


main()
