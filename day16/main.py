import itertools
import re


def main():
    input_file = open('input/day16.txt', 'r')
    ticket_lines = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    tickets_data = load_tickets_data(ticket_lines)

    print('Answer 1: {}'.format(get_tickets_error_rate(tickets_data)))

    valid_tickets = get_valid_tickets(tickets_data)
    fields = list(tickets_data['rules'].keys())

    field_sets = generate_full_guess_set(fields)
    reduce_guess_set(field_sets, tickets_data['rules'], valid_tickets)
    eliminate_duplicates(field_sets)
    field_names_ordered = [f[0] for f in field_sets]

    product = 1
    for field_name in field_names_ordered:
        if field_name.startswith('departure'):
            product *= get_ticket_field_by_name(tickets_data['my_ticket'], field_name, field_names_ordered)

    print('Answer 2: {}'.format(product))


def get_ticket_field_by_name(ticket, field_name, field_order):
    return ticket[field_order.index(field_name)]


def reduce_guess_set(field_sets, rules, valid_tickets):
    for i, field_set in enumerate(field_sets):
        for ticket in valid_tickets:
            for field in field_set[:]:
                if ticket[i] not in rules[field]:
                    field_set.remove(field)


def eliminate_duplicates(guess_sets):
    for i in range(len(guess_sets)):
        for j, guess_set in enumerate(guess_sets):
            if len(guess_set) == 1:
                for k, guess_set2 in enumerate(guess_sets):
                    if k != j and guess_set[0] in guess_set2:
                        guess_set2.remove(guess_set[0])


def generate_full_guess_set(fields):
    field_sets = []
    for i in range(len(fields)):
        field_sets.append(fields[:])
    return field_sets


def guess_order(guessed_fields, remaining_fields, rules, valid_tickets):
    if not is_valid_order(guessed_fields, rules, valid_tickets):
        return []
    elif not remaining_fields:
        return guessed_fields
    else:
        for i, remaining_field in enumerate(remaining_fields):
            new_remaining_fields = remaining_fields[:i] + remaining_fields[i+1:]
            new_guess_fields = guessed_fields[:] + [remaining_field]
            new_guess_order = guess_order(new_guess_fields, new_remaining_fields, rules, valid_tickets)
            if new_guess_order:
                return new_guess_order


def is_valid_order(guessed_fields, rules, valid_tickets):
    for i, guessed_field in enumerate(guessed_fields):
        for ticket in valid_tickets:
            if ticket[i] not in rules[guessed_field]:
                return False
    return True


def get_valid_tickets(tickets_data):
    valid_tickets = []
    for ticket in tickets_data['near_tickets']:
        if not get_invalid_fields(tickets_data['rules'], ticket):
            valid_tickets.append(ticket)
    return valid_tickets


def get_tickets_error_rate(tickets_data):
    error_rate = 0
    for ticket in tickets_data['near_tickets']:
        error_rate += sum(get_invalid_fields(tickets_data['rules'], ticket))
    return error_rate


def get_invalid_fields(rules, ticket):
    invalid_fields = []
    for field in ticket:
        is_valid_field = False
        for rule in rules.values():
            if field in rule:
                is_valid_field = True
                break
        if not is_valid_field:
            invalid_fields.append(field)
    return invalid_fields


def load_tickets_data(ticket_lines):
    ticket_data = {'rules': {}, 'my_ticket': [], 'near_tickets': []}
    curr_line = 'rules'
    for line in ticket_lines:
        if line == '':
            continue
        elif line == 'your ticket:':
            curr_line = 'my_ticket'
            continue
        elif line == 'nearby tickets:':
            curr_line = 'near_tickets'
            continue
        elif curr_line == 'rules':
            r = re.match(r'([\w\s]*): (\d*)-(\d*) or (\d*)-(\d*)', line)
            rule = itertools.chain(range(int(r.group(2)), int(r.group(3)) + 1),
                                   range(int(r.group(4)), int(r.group(5)) + 1))
            ticket_data['rules'].update({r.group(1): list(rule)})
        elif curr_line == 'my_ticket':
            ticket_data['my_ticket'] = [int(num) for num in line.split(',')]
        elif curr_line == 'near_tickets':
            ticket_data['near_tickets'].append([int(num) for num in line.split(',')])

    return ticket_data


if __name__ == '__main__':
    main()
