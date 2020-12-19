def main():
    input_file = open('input/day18.txt', 'r')
    equations = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    eq_sum = 0
    for equation in equations:
        eq_sum += solve_equation(equation)
    print('Answer 1: {}'.format(eq_sum))


def solve_equation(equation):
    result, _ = solve_nested_equation(equation)
    return result


def solve_nested_equation(equation):
    lhs = 0
    op = '+'
    curr_offset = 0
    i = 0
    while i < len(equation):
        curr_offset += 1
        symbol = equation[i]
        i += 1
        if symbol in '0123456789':
            lhs = calculate(lhs, int(symbol), op)
        elif symbol in ['+', '*']:
            op = symbol
        elif symbol == '(':
            rhs, offset = solve_nested_equation(equation[i:])
            i += offset
            curr_offset += offset
            lhs = calculate(lhs, rhs, op)
        elif symbol == ')':
            return lhs, curr_offset
    return lhs, 0


def calculate(lhs, rhs, op):
    if op == '+':
        return lhs + rhs
    elif op == '*':
        return lhs * rhs


if __name__ == '__main__':
    main()
