import re
import math


def get_marked_questions(x: str) -> set:
    return set(re.findall(r'\w', x))


if __name__ == '__main__':
    file = open('./input.txt')
    groups = file.read().split('\n\n')

    print('Part 1', math.fsum([len(get_marked_questions(group)) for group in groups]))

    cnt = 0

    for group in groups:
        forms = [get_marked_questions(g) for g in group.splitlines()]
        unanimous = forms[0].intersection(*forms[1:])
        cnt = cnt + len(unanimous)

    print('Part 2', cnt)
