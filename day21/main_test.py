import unittest

from day21 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.foods_txt = [
            'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
            'trh fvjkl sbzzf mxmxvkd (contains dairy)',
            'sqjhc fvjkl (contains soy)',
            'sqjhc mxmxvkd sbzzf (contains fish)'
        ]

    def test_parse_foods_returns_correct_ingredients_and_allergens(self):
        actual = main.parse_foods(self.foods_txt)
        self.assertIn('mxmxvkd', actual[0]['ingredients'])
        self.assertIn('fish', actual[3]['allergens'])

    def test_get_all_items_returns_correct_set(self):
        foods = main.parse_foods(self.foods_txt)
        actual = main.get_all_items(foods, 'allergens')
        self.assertIn('soy', actual)
        self.assertEqual(len(actual), 3)

    def test_get_possible_allergens_returns_correct_data(self):
        foods = main.parse_foods(self.foods_txt)
        actual = main.get_possible_allergens(foods)
        self.assertEqual(actual['dairy'], set(['mxmxvkd']))
        self.assertEqual(actual['fish'], set(['mxmxvkd', 'sqjhc']))

    def test_reduce_all_allergens_returns_correct_data(self):
        foods = main.parse_foods(self.foods_txt)
        actual = main.get_possible_allergens(foods)
        main.reduce_all_allergens(actual)
        self.assertEqual(actual['fish'], set(['sqjhc']))
