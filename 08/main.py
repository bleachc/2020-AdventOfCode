import re


def calc_line_jmp(line: int, operator: str, n: int):
    return line + (-1 * n if operator == '-' else n)


def calc_acc(acc, operator, n):
    return acc - n if operator == '-' else acc + n


def execute(instructions: list, visits: set = None, line: int = 0, accumulator: int = 0):
    if visits is None:
        visits = set()

    if line == len(instructions) - 1:
        return True, accumulator

    if line in visits or 0 > line or line > len(instructions) - 1:
        return False, accumulator

    visits.add(line)

    operation, operator, n = instructions[line]
    n = int(n)

    if operation == 'nop':
        return execute(instructions, visits, line + 1, accumulator)
    elif operation == 'jmp':
        return execute(instructions, visits, calc_line_jmp(line, operator, n), accumulator)
    elif operation == 'acc':
        return execute(instructions, visits, line + 1, calc_acc(accumulator, operator, n))


if __name__ == '__main__':
    instructions = re.findall(r"(\w+) ([+-])(\d+)", open('./input.txt').read())

    print('Part 1', execute(instructions)[1])

    for i, line in enumerate(instructions):
        if line[0] == 'nop':
            alt = [*instructions]
            alt[i] = ('jmp', alt[i][1], alt[i][2])
            success, acc = execute(alt)

            if success:
                print('Part 2', acc)
        if line[0] == 'jmp':
            alt = [*instructions]
            alt[i] = ('nop', alt[i][1], alt[i][2])
            success, acc = execute(alt)

            if success:
                print('Part 2', acc)
