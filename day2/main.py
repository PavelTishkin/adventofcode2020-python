import re


def main():
    input_file = open('input/day2.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))

    valid_count = 0
    for file_line in file_lines:
        if check_password(file_line, 1):
            valid_count += 1
    print("Answer 1: {}".format(valid_count))

    valid_count = 0
    for file_line in file_lines:
        if check_password(file_line, 2):
            valid_count += 1
    print("Answer 2: {}".format(valid_count))


def check_password(input_str, check_type):
    """
    Check password validity based on check type selected
    :param input_str:
    :param check_type:
    :return:
    """
    # Parse out data from input string
    split1 = input_str.split(':')
    rule = split1[0].strip()
    password = split1[1].strip()
    split2 = rule.split()
    pass_range = split2[0].strip()
    pass_letter = split2[1].strip()
    split3 = pass_range.split('-')
    min_letter = int(split3[0].strip())
    max_letter = int(split3[1].strip())

    if check_type == 1:
        pattern = "[{}]".format(pass_letter)
        found_count = len(re.findall(pattern, password))

        if min_letter <= found_count <= max_letter:
            return True
        return False
    elif check_type == 2:
        if (password[min_letter-1] == pass_letter or password[max_letter-1] == pass_letter) \
                and not (password[min_letter-1] == pass_letter and password[max_letter-1] == pass_letter):
            return True
        return False


main()
