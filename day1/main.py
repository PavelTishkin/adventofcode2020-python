import functools


def main():
    input_file = open('input/day1.txt', 'r')
    file_lines = list(map(lambda l: int(l.strip()), input_file.readlines()))

    print("Answer 1: {}".format(sum_check(file_lines, 2020, 2, [])))

    print("Answer 2: {}".format(sum_check(file_lines, 2020, 3, [])))


def sum_check(input_list, target_sum, numbers_count, rec_list):
    """
    Return product of *numbers_count* numbers where sum of those numbers is equals to *target_sum*
    :param input_list:
    :param target_sum:
    :param numbers_count:
    :param rec_list:
    :return:
    """
    if numbers_count == 1:
        for i in range(len(input_list)):
            tmp_sum = functools.reduce(lambda x, y: x+y, rec_list)
            if input_list[i] + tmp_sum == target_sum:
                return functools.reduce(lambda x, y: x * y, rec_list) * input_list[i]
        return -1
    else:
        for i in range(len(input_list)-numbers_count+1):
            new_rec_list = rec_list.copy()
            new_rec_list.append(input_list[i])
            result = sum_check(input_list[i + 1:], target_sum, numbers_count - 1, new_rec_list)
            if result != -1:
                return result
        return -1


main()
