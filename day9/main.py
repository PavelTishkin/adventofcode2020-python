from functools import reduce


def main():
    input_file = open('input/day9.txt', 'r')
    numbers = list(map(lambda l: int(l.strip()), input_file.readlines()))

    weak_number = find_weak_number(numbers, 25)
    print('Answer 1: {}'.format(weak_number))

    encryption_weakness = find_encryption_weakness(numbers, weak_number)
    print('Answer 2: {}'.format(encryption_weakness))


def is_valid_sum(numbers, num_sum):
    for i, num1 in enumerate(numbers):
        for num2 in numbers[i:]:
            if num1 + num2 == num_sum:
                return True
    return False


def find_weak_number(numbers, step):
    for i in range(0, len(numbers)-step):
        if not is_valid_sum(numbers[i:i+step], numbers[i+step]):
            return numbers[i+step]
    raise Exception('No weak number found')


def find_encryption_weakness(numbers, weak_number):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)+1):
            arr_sum = sum_array(numbers[i:j])
            if arr_sum == weak_number:
                return min(numbers[i:j]) + max(numbers[i:j])
            if arr_sum > weak_number:
                break
    raise Exception('No encryption weakness found')


def sum_array(numbers):
    return reduce(lambda x, y: x+y, numbers)


if __name__ == '__main__':
    main()
