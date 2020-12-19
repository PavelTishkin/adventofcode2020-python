import unittest

from day18 import main


class MainTestCase(unittest.TestCase):

    def test_solve_simple_equation_returns_correct_values(self):
        eq = '1 + 2 * 3 + 4 * 5 + 6'
        actual = main.solve_equation(eq)
        self.assertEqual(actual, 71)

    def test_solve_nested_equation_returns_correct_values(self):
        eq = '1 + (2 * 3) + (4 * (5 + 6))'
        actual = main.solve_equation(eq)
        self.assertEqual(actual, 51)

    def test_solve_equation_starting_with_bracket_returns_correct_values(self):
        eq = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        actual = main.solve_equation(eq)
        self.assertEqual(actual, 13632)

