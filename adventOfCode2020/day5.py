class Seat:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.id = 0

    def __lt__(self, other):
        return self.id < other.id


def scan_seat(line):
    seat = Seat()

    # Make sure the line length is compatible with the hardcoded ranges
    if not len(line) == 10:
        print("Error: Line length:", len(line))
        return False

    for i in range(0, 7):
        if line[i] == "F":
            # Add a zero to the end
            seat.row = seat.row << 1
        if line[i] == "B":
            # Add a zero to the end
            seat.row = seat.row << 1
            # Add a one
            seat.row += 1

    for i in range(7, 10):
        if line[i] == "L":
            # Add a zero to the end
            seat.col = seat.col << 1
        if line[i] == "R":
            # Add a zero to the end
            seat.col = seat.col << 1
            # Add a one
            seat.col += 1

    seat.id = seat.row * 8 + seat.col
    return seat


def parse_seats(read_lines):
    all_seats = []

    for line in read_lines:
        # Load all the information into a seat object
        x = scan_seat(line)
        # Add the new populated seat to the list of seats
        all_seats.append(x)

    return all_seats


def find_missing_seat(all_seats):
    # Start from the lowest in the list
    previous = all_seats[0].id - 1

    for seat in all_seats:
        # Check to see if the seat id is sequential to the previous seat
        if not seat.id == (previous + 1):
            print("Missing seat:", seat.id - 1)
        # Set the previous to be the current seat id
        previous = seat.id


def find_highest_seat_id(all_seats: Seat):
    highest = 0

    for seat in all_seats:
        if seat.id > highest:
            highest = seat.id

    return highest


def load_seats():
    path = './inputs/day5.txt'

    with open(path, 'r') as file:
        read_lines = file.read().splitlines()

    # Parse the lines read to get the populated list of all the seats
    all_seats = parse_seats(read_lines)

    # Loop through the list of seats to find the highest value seat id
    highest = find_highest_seat_id(all_seats)
    print("Highest:", highest)

    # Sort all the seats using the class's "__lt__" function
    # This function sorts by seat id
    all_seats.sort()
    # Compare each seat id to the previous seat id to find the missing seat
    find_missing_seat(all_seats)


if __name__ == "__main__":
    load_seats()
