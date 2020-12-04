def find_tree(line, position):
    place = line[position]

    # Trees are represented by '#'
    if place == "#":
        return True
    return False

def scan_landscape(vector_x, vector_y):
    path = './inputs/day3.txt'
    position = 0
    tree_total = 0
    lines_crossed = 0

    with open(path, 'r') as file:
        tree_lines = file.read().splitlines()

        for line in tree_lines:
            pattern_length = len(line)

            # Instead of looping by delta y in the for loop
            # we are skipping lines which aren't multiples of the y delta
            if (lines_crossed % vector_y) == 0:
                # Make sure we stay within the repeating pattern
                pattern_position = position % pattern_length

                # Check for trees at the current position
                if find_tree(line, pattern_position):
                    tree_total += 1

                # Move to the next position
                position += vector_x

            # Tree lines crossed or in this case, the y position
            lines_crossed += 1
    return tree_total

if __name__ == "__main__":

    # Right 1, down 1.
    p1 = scan_landscape(1, 1)
    print("Right 1, down 1:", p1)

    # Right 3, down 1.
    p2 = scan_landscape(3, 1)
    print("Right 3, down 1:", p2)

    # Right 5, down 1.
    p3 = scan_landscape(5, 1)
    print("Right 5, down 1:", p3)

    # Right 7, down 1.
    p4 = scan_landscape(7, 1)
    print("Right 7, down 1:", p4)

    # Right 1, down 2.
    p5 = scan_landscape(1, 2)
    print("Right 1, down 2:", p5)

    total = p1 * p2 * p3 * p4 * p5
    print("total =", total)
