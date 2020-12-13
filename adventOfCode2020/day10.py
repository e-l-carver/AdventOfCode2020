counter = 0


# This method assumes there are no duplicates and therefore each number
#   can potentially have the three next numbers be within the 3 jolt limit
def chain_adapters(adapters: []):
    adapters_len_zeroed = len(adapters) - 1
    adapters_dict = {}

    # Sort the list in reverse so the largest is at the bottom
    # This just makes the for loop easier lol
    adapters.sort(reverse=True)

    # Set the first path entry as 1 to start off the process
    adapters_dict[adapters[0]] = 1

    # Paths are the number of paths to get to the end of the list from here
    # This is so we can just start from the highest and add up the paths
    #   rather than continually looping through the list
    for i in range(0, adapters_len_zeroed + 1):
        current = adapters[i]
        current_path = adapters_dict.get(current, 0)

        # We have reached the end! this should now contain all the possible paths
        if i == adapters_len_zeroed:
            return current_path

        # Check the next adapter to see if it is within 3 jolts
        if i + 1 <= adapters_len_zeroed:
            prev = adapters[i + 1]
            if current - prev <= 3:
                prev_path = adapters_dict.get(prev, 0)
                adapters_dict[prev] = prev_path + current_path

        # Check second away adapter to see if it is within 3 jolts
        if i + 2 <= adapters_len_zeroed:
            prev2 = adapters[i + 2]
            if current - prev2 <= 3:
                prev_path = adapters_dict.get(prev2, 0)
                adapters_dict[prev2] = prev_path + current_path

        # Check the third away adapter to see if it is within 3 jolts
        if i + 3 <= adapters_len_zeroed:
            prev3 = adapters[i + 3]
            if current - prev3 <= 3:
                prev_path = adapters_dict.get(prev3, 0)
                adapters_dict[prev3] = prev_path + current_path

    return False

    # This takes waaaaaaay too long :'(


def chain_adapters_no(adapters: [], index):
    total_adapters = len(adapters)

    if index == (total_adapters - 1):
        global counter
        counter += 1
        return

    if (index + 1) < total_adapters:
        if (adapters[index + 1] - adapters[index]) <= 3:
            chain_adapters(adapters, index + 1)

    if (index + 2) < total_adapters:
        if (adapters[index + 2] - adapters[index]) <= 3:
            chain_adapters(adapters, index + 2)

    if (index + 3) < total_adapters:
        if (adapters[index + 3] - adapters[index]) <= 3:
            chain_adapters(adapters, index + 3)

    return


def chain_adapters_simple(adapters: []):
    prev = 0
    diff_1 = 0
    diff_2 = 0
    diff_3 = 0

    for a in adapters:
        diff = a - prev

        if diff == 0:
            prev = a
        elif diff == 1:
            diff_1 += 1
        elif diff == 2:
            diff_2 += 1
        elif diff == 3:
            diff_3 += 1
        else:
            print("diff:", diff)
            return 0, 0, 0
        prev = a
    return diff_1, diff_2, diff_3


def part1():
    path = './inputs/day10.txt'
    adapters = []
    jolt_1 = 0
    jolt_2 = 0
    jolt_3 = 0

    with open(path, 'r') as file:
        read_lines = file.read().splitlines()

    # Add the socket
    adapters.append(0)
    for line in read_lines:
        adapters.append(int(line))

    adapters.sort()
    dev_jolt = adapters[len(adapters) - 1] + 3
    print("Device joltage:", dev_jolt)
    # Add the device
    adapters.append(dev_jolt)

    jolt_1, jolt_2, jolt_3 = chain_adapters_simple(adapters)

    print("Jolt-1:", jolt_1, "Jolt-2:", jolt_2, "Jolt-3:", jolt_3)
    print("Jolt-1 * Jolt-3:", jolt_1 * jolt_3)

    # chain_adapters_no(adapters, 0)
    # print("count", count)

    print("Total combinations:", chain_adapters(adapters))

    print("~~~~~end~~~~~")


if __name__ == "__main__":
    part1()
