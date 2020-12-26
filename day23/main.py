import sys
import numpy as np
from numba import njit, jit


def main():
    input_number = sys.argv[0]

    cup_sequence = [int(n) for n in list(input_number)]

    new_sequence = cup_sequence
    for i in range(100):
        new_sequence = cup_move(new_sequence)
    str_sequence = [str(n) for n in cup_shift_sequence(new_sequence, 1)]
    print('Answer 1: {}'.format(''.join(str_sequence)))

    sequence = generate_sequence_to_number(cup_sequence, 1000000)
    curr_idx = 0
    for i in range(10000000):
        sequence, curr_idx = cup_move_v2(sequence, curr_idx, 1000000)
    first_cup_idx = [i for i in range(len(sequence)) if sequence[i] == 1][0]
    sequence = cup_shift_sequence_v2(sequence, first_cup_idx)
    print('Answer 2: {}'.format(sequence[1] * sequence[2]))


def cup_move(cup_sequence):
    next_3 = cup_sequence[1:4]
    aligned_sequence = cup_sequence[0:1] + cup_sequence[4:]

    next_label = cup_sequence[0] - 1
    while next_label in next_3 or next_label == 0:
        next_label -= 1
        if next_label <= 0:
            next_label %= max(cup_sequence) + 1
    next_label_idx = aligned_sequence.index(next_label)
    next_sequence = aligned_sequence[:next_label_idx + 1] + next_3 + aligned_sequence[next_label_idx + 1:]
    next_sequence = next_sequence[1:] + next_sequence[0:1]

    return next_sequence


def cup_move_v2(cup_sequence, curr_idx, max_sequence):
    if curr_idx > max_sequence - 4:
        cup_sequence = cup_shift_sequence_v2(cup_sequence, curr_idx)
        curr_idx = 0

    next_3 = cup_sequence[curr_idx + 1:curr_idx + 4]
    dst_label = cup_sequence[curr_idx] - 1

    while dst_label in next_3 or dst_label == 0:
        dst_label -= 1
        if dst_label <= 0:
            dst_label %= max_sequence + 1

    dst_idx = find_first(dst_label, cup_sequence)
    if dst_idx == -1:
        raise Exception('Could not find index')
    if dst_idx > curr_idx:
        next_sequence = np.concatenate([cup_sequence[:curr_idx + 1],
                                       cup_sequence[curr_idx + 4:dst_idx + 1],
                                       cup_sequence[curr_idx + 1:curr_idx + 4],
                                       cup_sequence[dst_idx + 1:]])
        dst_idx -= 3
    else:
        next_sequence = np.concatenate([cup_sequence[:dst_idx + 1],
                                       cup_sequence[curr_idx + 1:curr_idx + 4],
                                       cup_sequence[dst_idx + 1:curr_idx + 1],
                                       cup_sequence[curr_idx + 4:]])
        curr_idx += 3
    next_idx = curr_idx + 1

    return next_sequence, next_idx


@jit(nopython=True)
def find_first(item, vec):
    for i, v in enumerate(vec):
        if item == v:
            return i
    return -1


def cup_shift_sequence(cup_sequence, start_cup):
    start_cup_idx = [i for i in range(len(cup_sequence)) if cup_sequence[i] == start_cup][0]
    new_sequence = cup_sequence[start_cup_idx + 1:] + cup_sequence[:start_cup_idx + 1]
    return new_sequence[:-1]


def cup_shift_sequence_v2(cup_sequence, start_cup_idx):
    return np.concatenate([cup_sequence[start_cup_idx:],
                           cup_sequence[:start_cup_idx]])


def generate_sequence_to_number(start_sequence, max_number):
    new_sequence = start_sequence[:]
    for n in range(max(start_sequence) + 1, max_number + 1):
        new_sequence.append(n)
    return np.array(new_sequence)


if __name__ == '__main__':
    main()
