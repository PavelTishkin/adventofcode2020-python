import itertools


def main():
    input_file = open('input/day10.txt', 'r')
    adapter_list = list(map(lambda l: int(l.strip()), input_file.readlines()))
    # Prepare list of adapters by adding socket and device values and sorting
    add_jolts_min_max(adapter_list)
    adapter_list.sort()

    # Part 1 - count number of differences in jolts and multiply together
    diffs = count_jolt_diffs(adapter_list, 1, 3)
    print('Answer 1: {}'.format(diffs['1'] * diffs['3']))

    # Part 2 is a bit trickier. Observe from example that we can remove some adapters from the list with jolt diff of 1
    # E.g. with the following difference range 1-3-1-1-1-3-1-3 we have a contiguous range of 1-1-1 in the middle.
    # If we add two neighbouring 1's together, the chain is uninterrupted as long as total sum is not greater than 3
    # We also need to to ignore rightmost 1 in the sequence, since it's neighbour is 3, and the sum of 4 is too large
    # Some sequences can be long, e.g. 1-1-1-1-1, in those cases we also need to avoid using 3 values in a row,
    # since that would make a jolt gap of 4

    total_perms = 1
    # First, find all contiguous adapters, that have more that one adapter with jolt diff of 1
    ones_map = get_contiguous_map_of_ones(adapter_list)
    # For each of found sequences, determine valid permutations of adapters
    for ones in ones_map:
        # Multiply all found permutations to obtain total permutations value
        # Note: can be made more efficient by caching previous results
        total_perms *= get_valid_permutations_len(ones)
    print('Answer 2: {}'.format(total_perms))


def add_jolts_min_max(adapter_numbers):
    """
    Add minimum and maximum (+3) jolt values to adapter list
    :param adapter_numbers:
    :return:
    """
    adapter_numbers.append(0)
    adapter_numbers.append(max(adapter_numbers) + 3)


def count_jolt_diffs(adapters_list, *diffs):
    """
    Count number of jolt differences in an ordered list of adapters
    :param adapters_list: List of adapters
    :param diffs: Values of diffs to search for
    :return: Dictionary of jolt diffs and found count
    """
    result = dict((str(diff), 0) for diff in diffs)

    for i in range(len(adapters_list) - 1):
        diff = adapters_list[i+1] - adapters_list[i]
        if str(diff) in result.keys():
            result[str(diff)] += 1

    return result


def get_contiguous_map_of_ones(adapter_list):
    """
    Find contiguous number of adapters with jolt diff of 1 (excluding single occurences)
    :param adapter_list: List of adapters
    :return: List of contiguous number of adapters found
    """
    result = []
    next_range_count = 0
    for i in range(len(adapter_list)-1):
        if adapter_list[i+1] - adapter_list[i] == 1:
            next_range_count += 1
        elif next_range_count > 0:
            # Only interested in sequences of 2 or more
            if next_range_count > 1:
                result.append(next_range_count)
            next_range_count = 0
    return result


def get_valid_permutations_len(max_length):
    """
    Get list of valid permutations for which adapter we can remove from the list
    :param max_length: Max length of permutation list
    :return: Number of valid permutations
    """
    perms = list(itertools.product([0, 1], repeat=max_length-1))
    valid_perms = list(filter(is_valid_permutation, perms))
    return len(valid_perms)


def is_valid_permutation(perm):
    """
    Check if permutation is valid (does not contain 3 or more 1's in a row)
    :param perm: Permutation to check
    :return: True if valid
    """
    for i in range(len(perm) - 2):
        if perm[i] + perm[i+1] + perm[i+2] >= 3:
            return False
    return True


if __name__ == '__main__':
    main()
