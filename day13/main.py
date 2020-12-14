def main():
    input_file = open('input/day13.txt', 'r')
    timetables = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    current_timestamp = int(timetables[0])
    schedule = list(map(lambda t: int(t) if t != 'x' else 0, timetables[1].split(',')))

    next_departure = get_next_departure(current_timestamp, schedule)
    print('Answer 1: {}'.format(next_departure[0] * (next_departure[1] - current_timestamp)))

    # TODO: Rewrite, as O(n) doesn't work for large inputs
    #first_sequential_departure = get_first_timestamp_sequential_departure(schedule)
    #print('Answer 2: {}'.format(first_sequential_departure))


def get_bus_departure(curr_timestamp, bus_id):
    departure_offset = curr_timestamp % bus_id
    if departure_offset == 0:
        return curr_timestamp
    else:
        return curr_timestamp + bus_id - curr_timestamp % bus_id


def get_next_departure(curr_timestamp, schedule):
    departures = get_all_departures(curr_timestamp, schedule)
    first_departure = min(departures.values())
    first_bus_id = [bus_id for bus_id in departures if departures[bus_id] == first_departure][0]
    return first_bus_id, first_departure


def get_all_departures(curr_timestamp, schedule):
    departures = {}
    for bus_id in schedule:
        if bus_id == 0:
            continue
        departures[bus_id] = get_bus_departure(curr_timestamp, bus_id)
    return departures


def has_timestamp_sequential_departure(timestamp, schedule):
    for i, bus_id in enumerate(schedule):
        if bus_id != 0 and get_bus_departure(timestamp, bus_id) != timestamp + i:
            return False
    return True


def get_first_timestamp_sequential_departure(schedule):
    timestamp = 0
    while True:
        if has_timestamp_sequential_departure(timestamp, schedule):
            return timestamp
        timestamp += 1


if __name__ == '__main__':
    main()
