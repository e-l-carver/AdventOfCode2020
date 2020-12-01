int_lines = []
path = 'C:\\Users\\lilly\\PycharmProjects\\AdventOfCode2020\\adventOfCode2020\\inputs\\day1.txt'
with open(path, 'r') as file:
    read_lines = file.read().splitlines()
    for line in read_lines:
        int_lines.append(int(line))

for i in int_lines:
    for j in int_lines:
        for k in int_lines:
            total = i+j+k
            if total == 2020:
                print(i*j*k)
