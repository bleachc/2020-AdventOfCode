import re


def isValid(line):
    matches = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    min = int(matches.group(1))
    max = int(matches.group(2))
    seek = matches.group(3)
    password = matches.group(4)

    seek_cnt = len([c for c in password if c == seek])

    if min <= seek_cnt <= max:
        return True

    return False


def isValidTwo(line):
    matches = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    a = int(matches.group(1))
    b = int(matches.group(2))
    seek = matches.group(3)
    password = matches.group(4)

    if password[a - 1] == seek and password[b - 1] != seek:
        return True
    if password[a - 1] != seek and password[b - 1] == seek:
        return True

    return False


if __name__ == '__main__':
    with open('./input.txt') as f:
        lines = f.readlines()

        valid_cnt = 0

        for line in lines:
            if isValid(line):
                valid_cnt = valid_cnt + 1

        print(valid_cnt)

        valid_cnt_two = 0

        for line in lines:
            if isValidTwo(line):
                valid_cnt_two = valid_cnt_two + 1

        print(valid_cnt_two)
