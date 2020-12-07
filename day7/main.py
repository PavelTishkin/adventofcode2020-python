import re


class BagObject:

    def __init__(self):
        self.color = ""
        self.contents = []
        self.held_by = set()

    def __repr__(self):
        return f'{self.color, self.contents, self.held_by}'

    def get_contents_colors(self):
        return [c['bag'].color for c in self.contents]

    def get_held_by_colors(self):
        return list(self.held_by)


def main():
    input_file = open('input/day7.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))

    bags_list = {}
    for file_line in file_lines:
        parse_bag_rule(file_line, bags_list)

    gold_bag = bags_list['shiny gold']
    print("Answer 1: {}".format(len(count_outer_bags(gold_bag, bags_list))))
    print("Answer 2: {}".format(count_inner_bags(gold_bag, bags_list) - 1))


def parse_bag_rule(bag_rule, bags_list):
    r = re.match(r'([\w\s]*) bags contain (.*).', bag_rule)
    if r:
        # Extract bag color
        bag_color = r.group(1)
        # If bag already in the list, use the reference, otherwise create and add new bag
        if bag_color in bags_list.keys():
            bag = bags_list[bag_color]
        else:
            bag = BagObject()
            bags_list[bag_color] = bag
        bag.color = bag_color
        # If bag does not hold other bags
        if r.group(2) == 'no other bags':
            bag.contents = []
        else:
            # Get bag contents
            for bag_contents in r.group(2).split(','):
                r = re.match(r'(\d*) ([\w\s]*) bag', bag_contents.strip())
                held_bag_count = int(r.group(1))
                held_bag_color = r.group(2)
                # Use existing sub bag reference if color found, else create a new one
                if held_bag_color in bags_list.keys():
                    sub_bag = bags_list[held_bag_color]
                else:
                    sub_bag = BagObject()
                    sub_bag.color = held_bag_color
                    bags_list[held_bag_color] = sub_bag
                bag.contents.append({'bag': sub_bag, 'count': held_bag_count})
                sub_bag.held_by.add(bag_color)

    else:
        raise Exception("Bag color not detected")


def update_held_by(bag, bags_list):
    for bag_color in bags_list.keys():
        if bag.color in bags_list[bag_color].get_contents_colors():
            bag.held_by[bag_color] = bags_list[bag_color]


def count_outer_bags(bag, bags_list):
    held_by_combined = set()
    for parent_bag_color in bag.get_held_by_colors():
        held_by_combined.add(parent_bag_color)
        held_by_combined.update(count_outer_bags(bags_list[parent_bag_color], bags_list))
    return held_by_combined


# Make sure to subtract 1 at the end, because count includes self
def count_inner_bags(bag, bags_list):
    total_bags_count = 1
    for inner_bag in bag.contents:
        total_bags_count += inner_bag['count'] * count_inner_bags(inner_bag['bag'], bags_list)

    return total_bags_count


if __name__ == '__main__':
    main()
