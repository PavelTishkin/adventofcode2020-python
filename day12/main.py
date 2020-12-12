def main():
    input_file = open('input/day12.txt', 'r')
    directions = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    ship = Ship()
    for instruction in directions:
        ship.move(instruction)
    print('Answer 1: {}'.format(ship.get_manhattan_distance()))

    ship = Ship()
    for instruction in directions:
        ship.move_with_waypoint(instruction)
    print('Answer 2: {}'.format(ship.get_manhattan_distance()))


class Ship:

    def __init__(self):
        self.direction = 90
        self.x = 0
        self.y = 0
        self.wp_x = 10
        self.wp_y = 1

    def move(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            self.y += value
        elif action == 'S':
            self.y -= value
        elif action == 'E':
            self.x += value
        elif action == 'W':
            self.x -= value
        elif action == 'L':
            self.direction -= value
            if self.direction < 0:
                self.direction += 360
        elif action == 'R':
            self.direction += value
            if self.direction >= 360:
                self.direction -= 360
        elif action == 'F':
            if self.direction == 0:
                self.move(f'N{value}')
            elif self.direction == 90:
                self.move(f'E{value}')
            elif self.direction == 180:
                self.move(f'S{value}')
            elif self.direction == 270:
                self.move(f'W{value}')

    def move_with_waypoint(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            self.wp_y += value
        elif action == 'S':
            self.wp_y -= value
        elif action == 'E':
            self.wp_x += value
        elif action == 'W':
            self.wp_x -= value
        elif action in ('L', 'R'):
            rotate = value
            if action == 'L':
                rotate = 360 - rotate
            if rotate == 90:
                tmp = self.wp_x
                self.wp_x = self.wp_y
                self.wp_y = tmp * -1
            elif rotate == 180:
                self.wp_x = self.wp_x * -1
                self.wp_y = self.wp_y * -1
            elif rotate == 270:
                tmp = self.wp_x
                self.wp_x = self.wp_y * -1
                self.wp_y = tmp
        elif action == 'F':
            self.x += self.wp_x * value
            self.y += self.wp_y * value

    def get_manhattan_distance(self):
        return abs(self.x) + abs(self.y)


if __name__ == '__main__':
    main()
