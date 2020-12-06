class Form:
    def __init__(self, answers: str):
        self.answers = answers
        self.full_answers = [False] * 26
        self.binary = 0


def convert_form(form_input):
    # Make this answer into the 'Form' class for easier data management
    form = Form(form_input)

    # Populate the 'full_answers' list with True or False
    # for each of the questions
    for answer in form.answers:
        # Ord() returns the UNICODE value for the letter
        # This assumes that the letters are only lowercase and all valid
        # We minus '97' which is the unicode character for 'a' so that a == 0 and so on
        i = ord(answer) - 97
        form.full_answers[i] = True

    # Convert the full form into binary where each digit represents a question
    for q in form.full_answers:
        form.binary = form.binary << 1
        if q:
            form.binary += 1
    return form


def compare_group_any(group):
    group_score = group[0].binary

    # Compare all the scores to see if anyone marked 'yes' to a letter
    for form in group:
        group_score = form.binary | group_score

    total = bin(group_score).count("1")
    return total


def compare_group_all(group):
    group_score = group[0].binary

    # Compare all the scores to see if everyone marked 'yes' to a letter
    for form in group:
        group_score = form.binary & group_score

    total = bin(group_score).count("1")
    return total


def handle_group(line):
    # Split up the group into the individual responses
    people = line.split("\n")
    group = []

    # Go through each person and convert their scores into a better format
    # Then add the converted people to a list for better comparisons
    for form_input in people:
        group.append(convert_form(form_input))

    # For Part 1 we check how many questions someone answered 'yes' to
    # For Part 2 we check how many questions everyone answered 'yes' to
    return compare_group_any(group), compare_group_all(group)


def load_forms():
    path = './inputs/day6.txt'
    total_any = 0
    total_all = 0

    # Groups of people are split by empty lines
    with open(path, 'r') as file:
        read_lines = file.read().split("\n\n")

    for line in read_lines:
        total_any += handle_group(line)[0]
        total_all += handle_group(line)[1]

    print("total_any:", total_any)
    print("total_all:", total_all)


if __name__ == "__main__":
    load_forms()
