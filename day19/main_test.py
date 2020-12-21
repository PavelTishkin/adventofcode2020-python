import unittest

from day19 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.rules_messages = [
            '0: 4 1 5',
            '1: 2 3 | 3 2',
            '2: 4 4 | 5 5',
            '3: 4 5 | 5 4',
            '4: "a"',
            '5: "b"',
            '',
            'ababbb',
            'bababa',
            'abbbab',
            'aaabbb',
            'aaaabbb'
        ]

        input_file = open('input/day19_test.txt', 'r')
        self.rules_messages_rec = list(map(lambda l: l.strip(), input_file.readlines()))
        input_file.close()

    def test_parse_rule_returns_correct_leaf_rule(self):
        actual = main.parse_rule('4: "a"')
        self.assertEqual(actual.rule_id, 4)
        self.assertEqual(actual.rule_type, 'leaf')
        self.assertEqual(actual.leaf_letter, 'a')

    def test_parse_rule_returns_correct_branch_rule(self):
        actual = main.parse_rule('1: 2 3 | 3 2')
        self.assertEqual(actual.rule_id, 1)
        self.assertEqual(actual.rule_type, 'branch')
        self.assertEqual(actual.left_branch_ids, [2, 3])
        self.assertEqual(actual.right_branch_ids, [3, 2])

    def test_parse_rule_returns_correct_trunk_rule(self):
        actual = main.parse_rule('0: 4 1 5')
        self.assertEqual(actual.rule_id, 0)
        self.assertEqual(actual.rule_type, 'trunk')
        self.assertEqual(actual.trunk_ids, [4, 1, 5])

    def test_parse_rules_messages_returns_correct_data(self):
        rules, messages = main.parse_rules_messages(self.rules_messages)
        self.assertEqual(rules[1].rule_id, 1)
        self.assertIn("ababbb", messages)
        self.assertIn("aaaabbb", messages)

    def test_link_rules_creates_correct_trunk_chain(self):
        rules, _ = main.parse_rules_messages(self.rules_messages)
        rule = rules[0]
        rule.link_rules(rules)
        self.assertEqual(rule.trunk_rules[0].rule_id, 4)
        self.assertEqual(rule.trunk_rules[2].rule_id, 5)

    def test_link_rules_creates_correct_branch_chain(self):
        rules, _ = main.parse_rules_messages(self.rules_messages)
        rule = rules[1]
        rule.link_rules(rules)
        self.assertEqual(rule.left_branch_rules[0].rule_id, 2)
        self.assertEqual(rule.right_branch_rules[0].rule_id, 3)

    def test_match_messages_matches_leaf_rule(self):
        rule = main.Rule(0, 'leaf', leaf_letter='a')
        messages = main.init_messages_remainders(['a', 'b', 'aa'])
        actual = rule.match_messages(messages)
        self.assertIn('a', actual.keys())
        self.assertNotIn('b', actual.keys())
        self.assertIn('', actual['a'])
        self.assertIn('a', actual['aa'])

    def test_match_messages_matches_branch_rule(self):
        rules_messages = [
            '0: 1 2 | 2 1', '1: "a"', '2: "b"', '',
            'a', 'b', 'ab', 'ba', 'aba', 'bab', 'aab', 'bba', 'bbab']
        rules, messages = main.parse_rules_messages(rules_messages)
        main.link_rules(rules)
        rule = rules[0]
        messages = main.init_messages_remainders(messages)
        actual = rule.match_messages(messages)
        self.assertIn('ab', actual.keys())
        self.assertIn('aba', actual.keys())
        self.assertIn('ba', actual.keys())
        self.assertIn('bab', actual.keys())
        self.assertNotIn('a', actual.keys())
        self.assertNotIn('b', actual.keys())
        self.assertNotIn('aab', actual.keys())
        self.assertNotIn('bba', actual.keys())
        self.assertNotIn('bbab', actual.keys())
        self.assertIn('', actual['ab'])
        self.assertIn('', actual['ba'])
        self.assertIn('a', actual['aba'])
        self.assertIn('b', actual['bab'])

    def test_match_messages_matches_trunk_rule(self):
        rules_messages = [
            '0: 1 3', '1: 2', '2: "a"', '3: "b"', '',
            'ab', 'a', 'b', 'ba', 'aba', 'abb']
        rules, messages = main.parse_rules_messages(rules_messages)
        main.link_rules(rules)
        rule = rules[0]
        messages = main.init_messages_remainders(messages)
        actual = rule.match_messages(messages)
        self.assertIn('ab', actual.keys())
        self.assertIn('aba', actual.keys())
        self.assertIn('abb', actual.keys())
        self.assertNotIn('a', actual.keys())
        self.assertNotIn('b', actual.keys())
        self.assertNotIn('ba', actual.keys())
        self.assertIn('', actual['ab'])
        self.assertIn('a', actual['aba'])

    def test_match_messages_matched_combined_rules(self):
        rules, messages = main.parse_rules_messages(self.rules_messages)
        main.link_rules(rules)
        rule = rules[0]
        messages = main.init_messages_remainders(messages)
        matched_messages = rule.match_messages(messages)
        actual = main.discard_messages_with_remainders(matched_messages)
        self.assertIn('ababbb', actual.keys())
        self.assertIn('abbbab', actual.keys())
        self.assertNotIn('bababa', actual.keys())
        self.assertNotIn('aaabbb', actual.keys())
        self.assertNotIn('aaaabbb', actual.keys())

    def test_match_messages_non_recursive_rules(self):
        rules, messages = main.parse_rules_messages(self.rules_messages_rec)
        main.link_rules(rules)
        rule = rules[0]
        messages = main.init_messages_remainders(messages)
        matched_messages = rule.match_messages(messages)
        actual = main.discard_messages_with_remainders(matched_messages)
        self.assertIn('bbabbbbaabaabba', actual.keys())
        self.assertIn('ababaaaaaabaaab', actual.keys())
        self.assertIn('ababaaaaabbbaba', actual.keys())
        self.assertEqual(len(actual.keys()), 3)

    def test_match_messages_recursive_rules(self):
        rules, messages = main.parse_rules_messages(self.rules_messages_rec)
        rules[8] = main.Rule(8, 'branch', [[42], [42, 8]])
        rules[11] = main.Rule(11, 'branch', [[42, 31], [42, 11, 31]])
        main.link_rules(rules)
        rule = rules[0]
        messages = main.init_messages_remainders(messages)
        matched_messages = rule.match_messages(messages)
        actual = main.discard_messages_with_remainders(matched_messages)
        self.assertIn('bbabbbbaabaabba', actual.keys())
        self.assertIn('babbbbaabbbbbabbbbbbaabaaabaaa', actual.keys())
        self.assertIn('aaabbbbbbaaaabaababaabababbabaaabbababababaaa', actual.keys())
        self.assertIn('bbbbbbbaaaabbbbaaabbabaaa', actual.keys())
        self.assertIn('bbbababbbbaaaaaaaabbababaaababaabab', actual.keys())
        self.assertIn('ababaaaaaabaaab', actual.keys())
        self.assertIn('ababaaaaabbbaba', actual.keys())
        self.assertIn('baabbaaaabbaaaababbaababb', actual.keys())
        self.assertIn('abbbbabbbbaaaababbbbbbaaaababb', actual.keys())
        self.assertIn('aaaaabbaabaaaaababaa', actual.keys())
        self.assertIn('aaaabbaabbaaaaaaabbbabbbaaabbaabaaa', actual.keys())
        self.assertIn('aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba', actual.keys())
