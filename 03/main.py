import math


def has_tree(map, x, y):
    return map[y][x] == '#'


def print_map(map):
    txt = ''

    for row in map:
        txt = txt + ''.join(row) + '\n'

    print txt


def extend_map(map, xv, yv):
    iterations = math.ceil(len(map) / yv)
    extensions = math.ceil(iterations * xv / len(map[0]))

    ex = []

    for row in map:
        nr = []

        for _ in range(int(extensions)):
            nr = nr + row

        ex.append(nr)

    return ex


def count_trees(map, cur_x, cur_y, xv, yv):
    max_y = len(map) - 1
    extended_map = extend_map(map, xv, yv)

    tree_count = 0

    while True:
        cur_x, cur_y = cur_x + xv, cur_y + yv

        if 0 < cur_y > max_y:
            print_map(extended_map)
            return tree_count

        tree_count = tree_count + 1 if has_tree(extended_map, cur_x, cur_y) else tree_count
        extended_map[cur_y][cur_x] = 'X' if has_tree(extended_map, cur_x, cur_y) else 'O'


if __name__ == '__main__':
    with open('./input.txt') as f:
        map = [[column for column in row if column != '\n'] for row in f.readlines()]

        print('Part 1: ', count_trees(map, 0, 0, 3, 1))

        a, b, c, d, e = (count_trees(map, 0, 0, 1, 1), count_trees(map, 0, 0, 3, 1), count_trees(map, 0, 0, 5, 1),
                         count_trees(map, 0, 0, 7, 1), count_trees(map, 0, 0, 1, 2))

        print('Part 2: ', a * b * c * d * e)
