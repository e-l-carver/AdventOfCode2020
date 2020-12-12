def find_min_max(group: []):
    min_num = group[0]
    max_num = group[0]

    for num in group:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num


def add_numbers_in_groups(numbers: [], target: int, group_size):
    max_index = len(numbers) - group_size
    lower_num = 0
    higher_num = 0

    for index in range(0, max_index):
        total = 0
        group = []
        for i in range(0, group_size):
            total += numbers[index + i]
            group.append(numbers[index + i])

        if total == target:
            lower_num, higher_num = find_min_max(group)
            print("Min:", lower_num, "Max:", higher_num, "Total:", lower_num + higher_num, "group size:", group_size)
            return True

    return False


def add_two_numbers(numbers: [], target):
    for x in numbers:
        for y in numbers:
            if not (x == y):
                if (x + y) == target:
                    return False

    return True


def part1_check(numbers: [], index, p_length):
    min_index = index - p_length
    possible_numbers = []
    target = int(numbers[index])

    if min_index < 0:
        return False

    for j in range(min_index, index):
        possible_numbers.append(int(numbers[j]))

    return add_two_numbers(possible_numbers, target)


def part1():
    path = './inputs/day9.txt'
    p_length = 25

    with open(path, 'r') as file:
        numbers = file.read().splitlines()

    total_len = len(numbers)

    for i in range(0, total_len):
        if i >= p_length:
            if part1_check(numbers, i, p_length):
                return numbers[i]


def part2(target: int):
    path = './inputs/day9.txt'
    numbers = []

    with open(path, 'r') as file:
        read_lines = file.read().splitlines()

    for line in read_lines:
        numbers.append(int(line))

    numbers_len = len(numbers)

    for i in range(2, numbers_len - 1):
        if add_numbers_in_groups(numbers, target, i):
            return True


if __name__ == "__main__":
    result = part1()
    print("Part1:", result)
    part2(int(result))
