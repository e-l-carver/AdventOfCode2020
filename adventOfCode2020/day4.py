import re


class Field:
    def __init__(self, name: str, regex: str):
        self.name = name
        self.value = ""
        self.regex = regex


class Passport:
    def __init__(self):
        self.fields = [Field("byr", "^(19[2-9][0-9]|200[012])$"),
                       Field("iyr", "^(201[0-9]|2020)$"),
                       Field("eyr", "^(202[0-9]|2030)$"),
                       Field("hgt", "^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$"),
                       Field("hcl", "^(#[0-9a-f]{6})$"),
                       Field("ecl", "^(amb|blu|brn|gry|grn|hzl|oth)$"),
                       Field("pid", "^([0-9]{9})$"),
                       Field("cid", "()")]


# Find the named field in the passport and populate it
def find_field(p: Passport, name, value):
    for field in p.fields:
        if name == field.name:
            field.value = value


# Check the field values against their regex
def is_passport_valid(p: Passport):
    for field in p.fields:
        if not re.search(field.regex, field.value):
            # If any field fails the validation then whole passport fails
            return False
    return True


def passport_validator(line):
    all_fields = line.split()
    # Create a fresh passport
    p = Passport()

    for field in all_fields:
        # name:value
        f = field.split(":")
        name = f[0]
        value = f[1]

        # Find and populate the correct field
        find_field(p, name, value)

    return is_passport_valid(p)


def load_passports():
    path = './inputs/day4.txt'
    total = 0

    with open(path, 'r') as file:
        # The passports can span over several lines so split by empty lines
        read_lines = file.read().split("\n\n")
        # Validate each passport
        for line in read_lines:
            if passport_validator(line):
                total += 1
    print("total:", total)


if __name__ == "__main__":
    load_passports()
