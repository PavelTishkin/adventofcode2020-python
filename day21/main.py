import re
from functools import reduce


def main():
    input_file = open('input/day21.txt', 'r')
    foods_txt = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    foods = parse_foods(foods_txt)
    possible_allergens = get_possible_allergens(foods)
    reduce_all_allergens(possible_allergens)
    allergens = [list(allergen)[0] for allergen in possible_allergens.values()]
    clean_ingredients_count = 0
    for food in foods:
        for ingredient in food['ingredients']:
            if ingredient not in allergens:
                clean_ingredients_count += 1
    print('Answer 1: {}'.format(clean_ingredients_count))

    allergen_ingredients = []
    sorted_allergens = sorted(possible_allergens.keys())
    for allergen in sorted_allergens:
        allergen_ingredients.append(list(possible_allergens[allergen])[0])
    print('Answer 2: {}'.format(','.join(allergen_ingredients)))


def get_all_items(foods, key):
    all_items = set()
    for food in foods:
        all_items.update(food[key])
    return all_items


def get_possible_allergens(foods):
    allergens_match = {}
    all_allergens = get_all_items(foods, 'allergens')
    for allergen in all_allergens:
        ingredients_match = set()
        for food in foods:
            if allergen in food['allergens']:
                if ingredients_match:
                    ingredients_match = ingredients_match.intersection(set(food['ingredients']))
                else:
                    ingredients_match = set(food['ingredients'])
        allergens_match[allergen] = ingredients_match
    return allergens_match


def reduce_all_allergens(allergens_match):
    while reduce_allergen_set(allergens_match):
        continue


def reduce_allergen_set(allergens_match):
    is_remove = False
    for allergen, ingredients in allergens_match.items():
        if len(ingredients) == 1:
            if remove_ingredients_except(allergens_match, allergen, list(ingredients)[0]):
                is_remove = True

    return is_remove


def remove_ingredients_except(allergens_match, except_allergen, ingredient):
    is_remove = False
    for allergen, ingredients in allergens_match.items():
        if allergen != except_allergen and ingredient in ingredients:
            ingredients.remove(ingredient)
            is_remove = True
    return is_remove


def parse_foods(foods_txt):
    foods = []
    for food_txt in foods_txt:
        r = re.match(r'(.*) \(contains (.*)\)', food_txt)
        foods.append({'ingredients': r.group(1).split(' '), 'allergens': r.group(2).split(', ')})
    return foods


if __name__ == '__main__':
    main()
