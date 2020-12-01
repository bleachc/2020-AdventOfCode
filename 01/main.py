def find_two(numbers, goal):
    for number in numbers:
        target = goal - number

        if target in numbers:
            return number, target

    return False


def find_three(numbers):
    for i, number in enumerate(numbers):
        goal = 2020 - number
        n = [x for j, x in enumerate(numbers) if i != j]

        result = find_two(n, goal)

        if result:
            return number, result[0], result[1]


if __name__ == '__main__':
    with open('./input.txt') as f:
        numbers = [int(l) for l in f.readlines()]
        a, b = find_two(numbers, 2020)
        c, d, e = find_three(numbers)

        print('two', a * b)
        print('three', c * d * e)
