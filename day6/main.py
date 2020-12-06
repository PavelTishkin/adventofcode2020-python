from functools import reduce


def main():
    input_file = open('input/day6.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))

    groups = parse_groups(file_lines, False)
    groups_sum = 0
    for group in groups:
        groups_sum += len(group)
    print("Answer 1: {}".format(groups_sum))

    groups = parse_groups(file_lines, True)
    groups_sum = 0
    for group in groups:
        groups_sum += len(group)
    print("Answer 2: {}".format(groups_sum))


def parse_groups(input_lines, everyone=False):
    group_collection = []
    group_lines = []
    for i, input_line in enumerate(input_lines):
        if input_line != "":
            group_lines.append(input_line)
        if input_line == "" or i == len(input_lines) - 1:
            group_collection.append(group_lines)
            group_lines = []

    group_answers = []
    for group in group_collection:
        if everyone:
            group_answer = set(letter for letter in group[0])
        else:
            group_answer = set()
        for person_answers in group:
            if everyone:
                group_answer = group_answer.intersection(set(letter for letter in person_answers))
            else:
                group_answer.update(set(letter for letter in person_answers))
        group_answers.append(group_answer)

    return group_answers


if __name__ == '__main__':
    main()