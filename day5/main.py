def main():
    input_file = open('input/day5.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))

    tickets = {}
    max_id = 0
    for file_line in file_lines:
        ticket = get_ticket_data(file_line)
        tickets[ticket['id']] = ticket
        if ticket['id'] > max_id:
            max_id = ticket['id']

    print("Answer 1: {}".format(max_id))

    ticket_ids = tickets.keys()
    for i in range(0, 127 * 8 + 7):
        if i not in ticket_ids and i - 1 in ticket_ids and i + 1 in ticket_ids:
            print("Answer 2: {}".format(i))


def get_ticket_data(ticket_str):
    ticket_data = {}
    r_min, r_max = 0, 127
    for r in ticket_str[0:6]:
        switcher = {
            'F': {r_min, (r_max + r_min + 1)/2 - 1},
            'B': {(r_max + r_min + 1)/2, r_max}
        }
        r_min, r_max = switcher.get(r, 'Invalid seat code ')
    if ticket_str[6] == 'F':
        ticket_data['row'] = int(r_min)
    else:
        ticket_data['row'] = int(r_max)

    c_min, c_max = 0, 7
    for c in ticket_str[7:9]:
        switcher = {
            'L': {c_min, (c_max + c_min + 1)/2 - 1},
            'R': {(c_max + c_min + 1)/2, c_max}
        }
        c_min, c_max = switcher.get(c, 'Invalid seat code ')
    if ticket_str[9] == 'L':
        ticket_data['col'] = int(c_min)
    else:
        ticket_data['col'] = int(c_max)

    ticket_data['id'] = ticket_data['row'] * 8 +  ticket_data['col']
    return ticket_data

main()