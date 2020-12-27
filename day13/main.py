from functools import reduce


def main():
    input_file = open('input/day13.txt', 'r')
    timetables = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    current_timestamp = int(timetables[0])
    schedule = list(map(lambda t: int(t) if t != 'x' else 0, timetables[1].split(',')))

    next_departure = get_next_departure(current_timestamp, schedule)
    print('Answer 1: {}'.format(next_departure[0] * (next_departure[1] - current_timestamp)))

    print('Answer 2: {}'.format(calculate_crt(schedule)))


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
    """
    Check if the buses in the schedule will leave one minute apart from each other, starting at *timestamp*
    :param timestamp:
    :param schedule:
    :return:
    """
    for i, bus_id in enumerate(schedule):
        if bus_id != 0 and get_bus_departure(timestamp, bus_id) != timestamp + i:
            return False
    return True


def calculate_crt(schedule):
    time_to_departure = {bus: -i % bus for i, bus in enumerate(schedule) if bus != 0}
    buses = list(reversed(sorted(time_to_departure)))

    sum = 0
    prod = reduce(lambda a, b: a * b, time_to_departure.keys())
    for bus in buses:
        p = prod // bus
        sum += time_to_departure[bus] * mul_inv(p, bus) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def get_first_timestamp_sequential_departure(schedule, start=0):
    earliest_timestamp = 0
    period = schedule[0]

    for i in range(1, len(schedule)):
        while True:
            stop_number = period * schedule[i]
            if schedule[i] == 0:
                break
            elif get_bus_departure(earliest_timestamp, schedule[i]) == earliest_timestamp + i:
                period *= schedule[i]
                break
            else:
                earliest_timestamp += period
            if earliest_timestamp > stop_number:
                raise Exception("Period exceeded product of numbers. Terminating...")

    return earliest_timestamp


def get_list_sequential_departures(schedule, departures_count=5):
    departures = [get_first_timestamp_sequential_departure(schedule)]
    for i in range(1, departures_count):
        departures.append(get_first_timestamp_sequential_departure(schedule, departures[len(departures) - 1] + 1))
    return departures


def get_max_period(schedule):
    period = 1
    for bus_id in schedule:
        if bus_id != 0:
            period *= bus_id
    return period


if __name__ == '__main__':
    main()
