import re


def parse_password_line(line):
    matches = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    return int(matches.group(1)), int(matches.group(2)), matches.group(3), matches.group(4)


def is_valid_part_one(line):
    minimum, maximum, seek, password = parse_password_line(line)
    return int(minimum) <= len([c for c in password if c == seek]) <= int(maximum)


def is_valid_part_two(line):
    a, b, seek, password = parse_password_line(line)
    return (password[a - 1] == seek) ^ (password[b - 1] == seek)


def count_valid(valid_function, lines):
    return len([line for line in lines if valid_function(line)])


if __name__ == '__main__':
    with open('./input.txt') as f:
        lines = f.readlines()

        print('Part 1 Answer: ', count_valid(is_valid_part_one, lines))
        print('Part 2 Answer: ', count_valid(is_valid_part_two, lines))
