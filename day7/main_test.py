import unittest

from day7 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.input_data = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]

    def test_parse_bag_rule_parses_no_bags_rule(self):
        bags_list = {}
        main.parse_bag_rule(self.input_data[7], bags_list)
        actual = bags_list["faded blue"]
        self.assertEqual(actual.color, "faded blue")
        self.assertEqual(actual.contents, [])

    def test_parse_bag_rule_parses_single_bags_rule(self):
        bags_list = {}
        main.parse_bag_rule(self.input_data[2], bags_list)
        actual = bags_list["bright white"]
        self.assertEqual(actual.color, "bright white")
        self.assertEqual(actual.contents[0]['bag'].color, "shiny gold")
        self.assertEqual(actual.contents[0]['count'], 1)

    def test_parse_bag_rule_parses_multiple_bags_rule(self):
        bags_list = {}
        main.parse_bag_rule(self.input_data[0], bags_list)
        actual = bags_list["light red"]
        self.assertEqual(actual.color, "light red")
        self.assertEqual(actual.contents[0]['bag'].color, "bright white")
        self.assertEqual(actual.contents[0]['count'], 1)
        self.assertEqual(actual.contents[1]['bag'].color, "muted yellow")
        self.assertEqual(actual.contents[1]['count'], 2)

    def test_count_outer_bags(self):
        bags_list = {}
        for input_line in self.input_data:
            main.parse_bag_rule(input_line, bags_list)

        gold_bag = bags_list['shiny gold']
        actual = main.count_outer_bags(gold_bag, bags_list)
        self.assertEqual(len(actual), 4)
        self.assertTrue("dark orange" in actual)

    def test_count_inner_bags(self):
        bags_list = {}
        for input_line in self.input_data:
            main.parse_bag_rule(input_line, bags_list)

        gold_bag = bags_list['shiny gold']
        # Includes self, therefore subtract 1
        actual = main.count_inner_bags(gold_bag, bags_list) - 1
        self.assertEqual(actual, 32)

