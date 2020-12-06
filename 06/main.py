import re
import math


def get_marked_questions(x: str) -> set:
    return set(re.findall(r'\w', x))


def count_unanimous(groups: list, i: int = 0, cnt: int = 0):
    forms = [get_marked_questions(g) for g in groups[i].splitlines()]
    unanimous = forms[0].intersection(*forms[1:])

    return count_unanimous(groups, i + 1, cnt + len(unanimous)) if i < len(groups) - 1 else cnt


if __name__ == '__main__':
    file = open('./input.txt')
    groups = file.read().split('\n\n')

    print('Part 1', math.fsum([len(get_marked_questions(group)) for group in groups]))
    print('Part 2', count_unanimous(groups))
