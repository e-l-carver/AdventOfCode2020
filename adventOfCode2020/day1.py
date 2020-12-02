def part1(int_lines):
    print("Part 1")
    for i in int_lines:
        for j in int_lines:
            total = i+j
            if total == 2020:
                print(i*j)


def part2(int_lines):
    print("Part 2")
    for i in int_lines:
        for j in int_lines:
            for k in int_lines:
                total = i + j + k
                if total == 2020:
                    print(i * j * k)

def read_file():
    int_lines = []
    path = './inputs/day1.txt'

    with open(path, 'r') as file:
        read_lines = file.read().splitlines()
        for line in read_lines:
            int_lines.append(int(line))
    return int_lines

if __name__ == "__main__":
    file_output = read_file()
    part1(file_output)
    part2(file_output)