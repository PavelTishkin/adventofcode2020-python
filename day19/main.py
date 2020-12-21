import re


def main():
    input_file = open('input/day19.txt', 'r')
    rules_messages_txt = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    rules, messages = parse_rules_messages(rules_messages_txt)
    link_rules(rules)
    rule = rules[0]
    messages = init_messages_remainders(messages)
    matched_messages = rule.match_messages(messages)
    matched_messages = discard_messages_with_remainders(matched_messages)
    print('Answer 1: {}'.format(len(matched_messages)))

    rules, messages = parse_rules_messages(rules_messages_txt)
    rules[8] = Rule(8, 'branch', linked_rules_ids=[[42], [42, 8]])
    rules[11] = Rule(11, 'branch', linked_rules_ids=[[42, 31], [42, 11, 31]])
    link_rules(rules)
    rule = rules[0]
    messages = init_messages_remainders(messages)
    matched_messages = rule.match_messages(messages)
    matched_messages = discard_messages_with_remainders(matched_messages)
    print('Answer 2: {}'.format(len(matched_messages)))


def parse_rules_messages(rules_messages_txt):
    is_rules = True
    rules = {}
    messages = []
    for line in rules_messages_txt:
        if line == '':
            is_rules = False
            continue
        if is_rules:
            rule = parse_rule(line)
            rules[rule.rule_id] = rule
        else:
            messages.append(line)
    return rules, messages


def parse_rule(rule_txt):
    r = re.match(r'(\d*): (.*)', rule_txt)
    rule_id = int(r.group(1))
    rules_str = r.group(2)
    r = re.match(r'"(.*)"', rules_str)
    if r:
        return Rule(rule_id, 'leaf', leaf_letter=r.group(1))
    if "|" in rules_str:
        rules_arr = rules_str.split('|')
        rule_ids = []
        for rule in rules_arr:
            rule_ids.append([int(r) for r in rule.strip().split(' ')])
        return Rule(rule_id, 'branch', linked_rules_ids=rule_ids)
    else:
        return Rule(rule_id, 'trunk', linked_rules_ids=[int(r) for r in rules_str.split(' ')])


def link_rules(rules):
    for rule in rules.values():
        rule.link_rules(rules)


def discard_messages_with_remainders(messages):
    return {message: remainder for message, remainder in messages.items() if '' in remainder}


def init_messages_remainders(messages):
    result_messages = {}
    for message in messages:
        result_messages[message] = set()
        result_messages[message].add(message)
    return result_messages


class Rule:
    """
    This class is used to represent a Rule.
    There exist 3 possible types of rules:
    a. Sequential or trunk rule composed of 1..n other rules, e.g. **0: 1 2 3**
    b. Split or branch rule composed of a sequence of two rules, of which at least one must be valid, e.g. **1: 2 3 | 3 2**
    c. Final or leaf rule, matching exactly one letter, e.g. **2: "a"**
    """

    def __init__(self, rule_id, rule_type, linked_rules_ids=[], leaf_letter=''):
        """
        Initialize rule
        :param rule_id: ID of a rule
        :param rule_type: Can be either leaf, branch or trunk
        :param linked_rules_ids: Contains either list of rule ids for trunk rule or two lists of ids for branch rule
        :param leaf_letter: Contains a single letter used by a leaf rule
        """
        self.rule_id = rule_id
        self.rule_type = rule_type
        if self.rule_type == 'leaf':
            self.is_leaf_rule = True
            self.leaf_letter = leaf_letter
        elif self.rule_type == 'branch':
            self.left_branch_ids = linked_rules_ids[0]
            self.right_branch_ids = linked_rules_ids[1]
            self.left_branch_rules = []
            self.right_branch_rules = []
        elif self.rule_type == 'trunk':
            self.trunk_ids = linked_rules_ids
            self.trunk_rules = []
        else:
            raise Exception('Unknown rule type')

    def match_messages(self, messages, depth=0):
        """
        Matches list of messages.
        Returns subset of messages valid according to current rule and remainder of unmatched message
        :param messages: List of messages to match, including remainder if previous rules have been applied
        :param depth: Optional parameter to detect recursive loops
        :return: List of valid messages and remainders
        """
        matched_messages = {}

        msg_list = [msg for msg in messages.keys()]
        if not msg_list:
            return matched_messages

        longest_msg = max([len(msg) for msg in msg_list])
        if depth > longest_msg:
            return matched_messages

        if self.rule_type == 'trunk':
            matched_messages = messages
            for rule in self.trunk_rules:
                matched_messages = rule.match_messages(matched_messages, depth+1)
        elif self.rule_type == 'branch':
            matched_left_messages = messages
            matched_right_messages = messages
            for rule in self.left_branch_rules:
                matched_left_messages = rule.match_messages(matched_left_messages, depth+1)
            for rule in self.right_branch_rules:
                matched_right_messages = rule.match_messages(matched_right_messages, depth+1)

            # Combine results of left and right branches
            matched_messages = {**matched_left_messages, **matched_right_messages}
            for message, _ in matched_messages.items():
                if message in matched_left_messages and message in matched_right_messages:
                    matched_messages[message] = matched_left_messages[message].union(matched_right_messages[message])

        elif self.rule_type == 'leaf':
            for message in messages:
                new_remainders = set()
                for remainder in messages[message]:
                    if remainder != '' and remainder[0] == self.leaf_letter:
                        new_remainders.add(remainder[1:])
                if len(new_remainders):
                    matched_messages[message] = new_remainders
        else:
            raise NotImplemented(f'Unknown rule type {self.rule_type} in match_messages()')

        return matched_messages

    def link_rules(self, rules_list):
        """
        Links current rule to other rules based on trunk or branch ids list
        :param rules_list: Dictionary of all the rules available
        """
        if self.rule_type == 'branch':
            for rule_id in self.left_branch_ids:
                self.left_branch_rules.append(rules_list[rule_id])
            for rule_id in self.right_branch_ids:
                self.right_branch_rules.append(rules_list[rule_id])
        elif self.rule_type == 'trunk':
            for rule_id in self.trunk_ids:
                self.trunk_rules.append(rules_list[rule_id])
        else:
            None

    def __eq__(self, other):
        """
        Two rules are equals if their ids equal
        """
        return self.rule_id == other.rule_id

    def __repr__(self):
        repr_str = f'(id: {self.rule_id}; type: {self.rule_type}; rule: '
        if self.rule_type == 'leaf':
            repr_str += self.leaf_letter
        elif self.rule_type == 'branch':
            repr_str += f'[{self.left_branch_ids} | {self.right_branch_ids}]'
        elif self.rule_type == 'trunk':
            repr_str += f'{self.trunk_ids}'
        repr_str += ')'
        return repr_str


if __name__ == '__main__':
    main()
