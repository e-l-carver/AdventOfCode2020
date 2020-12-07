import re

# WARNING - This is not efficient at all but I'm really tired so yeah
all_bags_no_duplicates = []
all_bags = []


class Bag:
    def __init__(self, name: str, bags: []):
        self.name = name
        self.bags = bags


def load_instruction_no_duplicates(instruction):
    no_bags_string = "( no other bags)"
    primary_bag_regex = "[ ]*([a-z ]*) (bag[s]*[.]*)"
    inside_bag_regex = "[ ]*([0-9]*) ([a-z ]*) (bag[s]*[.]*)"

    bags = instruction.split("contain")
    inside_list = []

    primary_bag = re.search(primary_bag_regex, bags[0]).group(1)
    inside_bags = bags[1].split(",")

    if len(inside_bags) == 1:
        if re.search(no_bags_string, inside_bags[0]):
            all_bags_no_duplicates.append(Bag(primary_bag, inside_list))
            return all_bags_no_duplicates

    for bag in inside_bags:
        b = re.search(inside_bag_regex, bag)
        # Group 1 is the number which we ignore for now
        # Group 2 contains the name of the bag
        inside_list.append(b.group(2))

    # Create a bag that contains the name of the bag and the list of the inside bags
    # Add the bag to the no duplicates list as this is for Part 1
    all_bags_no_duplicates.append(Bag(primary_bag, inside_list))
    return all_bags_no_duplicates


def load_instruction(instruction):
    no_bags_string = "( no other bags)"
    primary_bag_regex = "[ ]*([a-z ]*) (bag[s]*[.]*)"
    inside_bag_regex = "[ ]*([0-9]*) ([a-z ]*) (bag[s]*[.]*)"

    bags = instruction.split("contain")
    inside_list = []

    primary_bag = re.search(primary_bag_regex, bags[0]).group(1)
    inside_bags = bags[1].split(",")

    if len(inside_bags) == 1:
        if re.search(no_bags_string, inside_bags[0]):
            all_bags.append(Bag(primary_bag, inside_list))
            return all_bags

    for bag in inside_bags:
        b = re.search(inside_bag_regex, bag)
        # Group 1 contains the number of bags
        num = int(b.group(1))
        for x in range(0, num):
            # Group 2 contains the name of the bag
            inside_list.append(b.group(2))

    # Create a bag that contains the name of the bag and the list of the inside bags
    all_bags.append(Bag(primary_bag, inside_list))
    return all_bags


def open_bag(a_bag: Bag, name):
    for b in a_bag.bags:
        if b == name:
            return True
        bag = find_bag_no_duplicates(b)
        if bag is not None:
            if open_bag(bag, name):
                return True
    return False


def open_bag_count(a_bag: Bag, counter):
    for b in a_bag.bags:
        bag = find_bag(b)
        if bag is not None:
            counter = open_bag_count(bag, counter)
    counter += 1
    return counter


def find_bag(name):
    for bag in all_bags:
        if bag.name == name:
            return bag
    return None


def find_bag_no_duplicates(name):
    for bag in all_bags_no_duplicates:
        if bag.name == name:
            return bag
    return None


def load_bags():
    path = './inputs/day7.txt'
    p1_count = 0
    p2_count = 0

    with open(path, 'r') as file:
        read_lines = file.read().split("\n")

    for instruction in read_lines:
        load_instruction(instruction)
        load_instruction_no_duplicates(instruction)

    for bag in all_bags_no_duplicates:
        if open_bag(bag, "shiny gold"):
            p1_count+=1
    print("P1 count:", p1_count)

    gold_bag = find_bag("shiny gold")
    p2_count = open_bag_count(gold_bag, p2_count)
    # Minus one to negate the "shiny gold bag" its self
    print("P2 count:", p2_count - 1)


if __name__ == "__main__":
    load_bags()
