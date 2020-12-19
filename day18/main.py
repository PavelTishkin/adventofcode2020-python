def main():
    input_file = open('input/day18.txt', 'r')
    equations = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    eq_sum = 0
    for equation in equations:
        eq = Equation(equation)
        eq_sum += eq.answer
    print('Answer 1: {}'.format(eq_sum))

    eq_sum = 0
    for equation in equations:
        eq = Equation(equation, True)
        eq_sum += eq.answer
    print('Answer 2: {}'.format(eq_sum))


class Equation:

    def __init__(self, equation_text, is_addition_preference=False):
        self.equation_text = equation_text
        self.is_addition_preference = is_addition_preference
        self.elements = []
        self.answer = 0
        self.extract_elements()
        self.solve()

    def extract_elements(self):
        ptr = 0
        while ptr < len(self.equation_text):
            symbol = self.equation_text[ptr]
            if symbol in '0123456789':
                self.elements.append(int(symbol))
            elif symbol in ['+', '*']:
                self.elements.append(symbol)
            elif symbol == '(':
                sub_equation = Equation(self.equation_text[ptr+1:], self.is_addition_preference)
                ptr += len(sub_equation.equation_text) + 1
                self.elements.append(sub_equation.answer)
                None
            elif symbol == ')':
                self.equation_text = self.equation_text[0:ptr]
                break
            ptr += 1

    def solve(self):
        if self.is_addition_preference:
            reduced_elements = self.reduce_for_ops(['+'])
            reduced_elements = self.reduce_for_ops(['*'], reduced_elements)
        else:
            reduced_elements = self.reduce_for_ops(['+', '*'])

        self.answer = reduced_elements[0]

    def reduce_for_ops(self, ops, elements=[]):
        reduced_elements = elements[:]
        if not elements:
            reduced_elements = self.elements[:]
        while any(op in reduced_elements for op in ops):
            for ptr, symbol in enumerate(reduced_elements):
                if symbol in ops:
                    lhs = reduced_elements[ptr - 1]
                    rhs = reduced_elements[ptr + 1]
                    lhs = self.calculate(lhs, rhs, symbol)
                    new_reduced_elements = []
                    if ptr > 2:
                        new_reduced_elements = reduced_elements[:ptr-1]
                    new_reduced_elements.append(lhs)
                    new_reduced_elements.extend(reduced_elements[ptr+2:])
                    reduced_elements = new_reduced_elements
                    break

        return reduced_elements

    @staticmethod
    def calculate(lhs, rhs, op):
        if op == '+':
            return lhs + rhs
        elif op == '*':
            return lhs * rhs

    def __repr__(self):
        return self.equation_text


if __name__ == '__main__':
    main()
