def part1_validater(password, letter, number_indicators):
    count = 0

    min = int(number_indicators[0])
    max = int(number_indicators[1])

    for c in password:
        if c == letter:
            count += 1

    return (count >= min) and (count <= max)

def part2_validater(password, letter, number_indicators):
    # One indexed numbers with a zero indexed array
    a = int(number_indicators[0]) - 1
    b = int(number_indicators[1]) - 1

    # This is a hacky way of doing an xor
    return ((password[a] == letter) != (password[b] == letter))

def line_parser(line):
    # layout of each line is:    "min-max l: password"
    line_list = line.split()
    password = line_list[2]
    letter = line_list[1][0]
    number_indicators = line_list[0].split("-")

    p1 = part1_validater(password, letter, number_indicators)
    p2 = part2_validater(password, letter, number_indicators)
    return (p1, p2)


def check_file():
    path = './inputs/day2.txt'
    part1_total = 0
    part2_total = 0

    with open(path, 'r') as file:
        read_lines = file.read().splitlines()
        for line in read_lines:
            r1, r2 = line_parser(line)
            if(r1):
                part1_total+=1
            if(r2):
                part2_total+=1

    print("Part1:", part1_total)
    print("Part2:", part2_total)

if __name__ == "__main__":
    check_file()