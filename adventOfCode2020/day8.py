import re
from enum import Enum

# No comments this time because it's super late.
# Figure it out I guess ¯\_(ツ)_/¯

inst_queue = []
global_acc = 0
list_len = 0


class Op(Enum):
    nop = 0,
    acc = 1,
    jmp = 2


class Instruction:
    def __init__(self, op, value: int):
        self.op = op
        self.value = value
        self.pos = -1

    def run_command(self, pos: int):
        if self.pos != -1:
            return False
        else:
            self.pos = pos

        if self.op == Op.jmp:
            return run_jmp(self.pos, self.value)
        elif self.op == Op.acc:
            return run_acc(self.pos, self.value)
        elif self.op == Op.nop:
            return run_nop(self.pos, self.value)


def run_jmp(pos, value):
    pos += value

    if pos >= list_len:
        return True
    return inst_queue[pos].run_command(pos)


def run_acc(pos, value):
    global global_acc
    global_acc += value

    pos += 1
    if pos >= list_len:
        return True
    return inst_queue[pos].run_command(pos)


def run_nop(pos, value):
    pos += 1
    if pos >= list_len:
        return True
    return inst_queue[pos].run_command(pos)


def replace_each_jmp():
    for inst in inst_queue:
        if inst.op == Op.jmp:
            inst.op = Op.nop
            if start_from_zero():
                return True
            inst.op = Op.jmp
    return False


def replace_each_nop():
    for inst in inst_queue:
        if inst.op == Op.nop:
            inst.op = Op.jmp
            if start_from_zero():
                return True
            inst.op = Op.nop
    return False


def start_from_zero():
    global global_acc
    global_acc = 0

    for inst in inst_queue:
        inst.pos = -1

    return inst_queue[0].run_command(0)


def format_instructions(line):
    inst_regex = "(acc|jmp|nop) ([\+\-])([0-9]+)"
    instruction = re.search(inst_regex, line)
    op = 0
    value = 0

    if instruction.group(1) == "jmp":
        op = Op.jmp
    elif instruction.group(1) == "acc":
        op = Op.acc
    elif instruction.group(1) == "nop":
        op = Op.nop

    if instruction.group(2) == "+":
        value = int(instruction.group(3))

    if instruction.group(2) == "-":
        value = (0 - int(instruction.group(3)))

    inst_queue.append(Instruction(op, value))


def load_instructions():
    path = './inputs/day8.txt'

    with open(path, 'r') as file:
        read_lines = file.read().split("\n")

    for line in read_lines:
        format_instructions(line)

    global list_len
    list_len = len(inst_queue)

    start_from_zero()
    print("Part1 acc:", global_acc)

    if replace_each_jmp():
        print("Part2 (replace jmp) acc:", global_acc)
    if replace_each_nop():
        print("Part2 (replace nop) acc:", global_acc)


if __name__ == "__main__":
    load_instructions()
