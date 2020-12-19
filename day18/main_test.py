import unittest

from day18 import main


class MainTestCase(unittest.TestCase):

    def test_solve_simple_equation_extracts_correct_elements(self):
        eq = main.Equation('1 + 2 * 3')
        self.assertEqual(eq.elements, [1, '+', 2, '*', 3])

    def test_reduce_for_ops_returns_correct_elements(self):
        eq = main.Equation('1 + 2 * 3')
        elements = eq.reduce_for_ops(['+'])
        self.assertEqual(elements, [3, '*', 3])

    def test_solve_equation_returns_correct_values(self):
        eq = main.Equation('1 + 2 * 3 + 4 * 5 + 6')
        self.assertEqual(eq.answer, 71)

    def test_solve_equation_returns_correct_values2(self):
        eq = main.Equation('1 + (2 * 3) + (4 * (5 + 6))')
        self.assertEqual(eq.answer, 51)

    def test_solve_equation_returns_correct_values3(self):
        eq = main.Equation('2 * 3 + (4 * 5)')
        self.assertEqual(eq.answer, 26)

    def test_solve_equation_returns_correct_values4(self):
        eq = main.Equation('5 + (8 * 3 + 9 + 3 * 4 * 3)')
        self.assertEqual(eq.answer, 437)

    def test_solve_equation_returns_correct_values5(self):
        eq = main.Equation('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
        self.assertEqual(eq.answer, 12240)

    def test_solve_equation_returns_correct_values6(self):
        eq = main.Equation('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
        self.assertEqual(eq.answer, 13632)

    def test_solve_equation_addition_preference_returns_correct_values1(self):
        eq = main.Equation('1 + 2 * 3 + 4 * 5 + 6', True)
        self.assertEqual(eq.answer, 231)

    def test_solve_equation_addition_preference_returns_correct_values2(self):
        eq = main.Equation('1 + (2 * 3) + (4 * (5 + 6))', True)
        self.assertEqual(eq.answer, 51)

    def test_solve_equation_addition_preference_returns_correct_values3(self):
        eq = main.Equation('2 * 3 + (4 * 5)', True)
        self.assertEqual(eq.answer, 46)

    def test_solve_equation_addition_preference_returns_correct_values4(self):
        eq = main.Equation('5 + (8 * 3 + 9 + 3 * 4 * 3', True)
        self.assertEqual(eq.answer, 1445)

    def test_solve_equation_addition_preference_returns_correct_values5(self):
        eq = main.Equation('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', True)
        self.assertEqual(eq.answer, 669060)

    def test_solve_equation_addition_preference_returns_correct_values6(self):
        eq = main.Equation('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', True)
        self.assertEqual(eq.answer, 23340)
