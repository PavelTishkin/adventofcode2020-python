def main():
    input_file = open('input/day15.txt', 'r')
    num_seq = list(map(lambda n: int(n), input_file.readlines()[0].split(',')))
    input_file.close()

    num = get_nth_number_with_lookup(num_seq, 2020)
    print('Answer 1: {}'.format(num))

    num = get_nth_number_with_lookup(num_seq, 30000000)
    print('Answer 2: {}'.format(num))


# Bruteforce approach
def get_numbers_sequence(start_sequence, sequence_length):
    sequence = start_sequence
    while len(sequence) < sequence_length:
        sequence.append(get_next_number(sequence))

    return sequence


def get_next_number(num_seq):
    last_number = num_seq[-1]
    occurrences = list(filter(lambda i: num_seq[i] == last_number, range(len(num_seq) - 1)))
    if last_number in num_seq[:-1]:
        return len(num_seq) - occurrences[-1] - 1
    else:
        return 0


# Lookup table approach
def init_lookup(num_seq):
    return {num: i for i, num in enumerate(num_seq)}


def get_next_number_with_lookup(last_num, offset, num_lookup):
    if last_num in num_lookup:
        result = offset - num_lookup[last_num]
        num_lookup[last_num] = offset
        return result
    else:
        num_lookup[last_num] = offset
        return 0


def get_nth_number_with_lookup(start_sequence, sequence_length):
    lookup = init_lookup(start_sequence[:-1])
    offset = len(start_sequence) - 1
    next_num = start_sequence[-1]
    while offset < sequence_length - 1:
        next_num = get_next_number_with_lookup(next_num, offset, lookup)
        offset += 1
    return next_num


if __name__ == '__main__':
    main()
