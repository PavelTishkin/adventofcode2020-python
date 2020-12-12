def main():
    input_file = open('input/day11.txt', 'r')
    seats = list(map(lambda l: list(l.strip()), input_file.readlines()))
    input_file.close()

    new_seats, is_flip = cycle_seats(seats)
    while is_flip:
        new_seats, is_flip = cycle_seats(new_seats)
    occupied_count = count_occupied_seats(new_seats)
    print('Answer 1: {}'.format(occupied_count))

    new_seats, is_flip = cycle_seats(seats, True)
    while is_flip:
        new_seats, is_flip = cycle_seats(new_seats, True)
    occupied_count = count_occupied_seats(new_seats)
    print('Answer 2: {}'.format(occupied_count))


def cycle_seats(seats, is_far=False):
    is_flip = False
    new_seats = generate_empty_seats(len(seats), len(seats[0]))
    for x in range(len(seats[0])):
        for y in range(len(seats)):
            curr_seat = seats[y][x]
            if is_far:
                if curr_seat == '#' and get_occupied_far_seats(x, y, seats) >= 5:
                    is_flip = True
                    curr_seat = 'L'
                elif curr_seat == 'L' and get_occupied_far_seats(x, y, seats) == 0:
                    is_flip = True
                    curr_seat = '#'
            else:
                if curr_seat == '#' and get_occupied_neighbour_seats(x, y, seats) >= 4:
                    is_flip = True
                    curr_seat = 'L'
                elif curr_seat == 'L' and get_occupied_neighbour_seats(x, y, seats) == 0:
                    is_flip = True
                    curr_seat = '#'

            new_seats[y][x] = curr_seat
    return new_seats, is_flip


def get_occupied_neighbour_seats(x, y, seats):
    occupied = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or i > len(seats[0])-1:
                continue
            if j < 0 or j > len(seats)-1:
                continue
            if i == x and j == y:
                continue
            if seats[j][i] == '#':
                occupied += 1

    return occupied


def get_occupied_far_seats(x, y, seats):
    occupied = 0
    if is_occupied_direction(x, y, -1, -1, seats):
        occupied += 1
    if is_occupied_direction(x, y, 0, -1, seats):
        occupied += 1
    if is_occupied_direction(x, y, 1, -1, seats):
        occupied += 1
    if is_occupied_direction(x, y, -1, 0, seats):
        occupied += 1
    if is_occupied_direction(x, y, 1, 0, seats):
        occupied += 1
    if is_occupied_direction(x, y, -1, 1, seats):
        occupied += 1
    if is_occupied_direction(x, y, 0, 1, seats):
        occupied += 1
    if is_occupied_direction(x, y, 1, 1, seats):
        occupied += 1
    return occupied


def is_occupied_direction(x, y, dir_x, dir_y, seats):
    check_x = x + dir_x
    check_y = y + dir_y
    while not is_out_of_range(check_x, check_y, seats):
        if seats[check_y][check_x] == '#':
            return True
        elif seats[check_y][check_x] == 'L':
            return False
        check_x += dir_x
        check_y += dir_y
    return False


def is_out_of_range(x, y, seats):
    return x < 0 or y < 0 or x >= len(seats[0]) or y >= len(seats)


def count_occupied_seats(seats):
    occupied_count = 0
    for seat_row in seats:
        for seat in seat_row:
            if seat == '#':
                occupied_count += 1
    return occupied_count


def generate_empty_seats(row_num, col_num):
    empty_seats = []
    for i in range(row_num):
        empty_seats.append(list('.' * col_num))
    return empty_seats


def print_seats(seats):
    for seat_row in seats:
        print(''.join(seat_row))
    print('')


if __name__ == '__main__':
    main()
