def has_sum_pair(target, window):
    pairs = [target - n for n in window]

    for i, number in enumerate(window):
        if number in set(pairs[:i] + pairs[i + 1:]):
            return True

    return False


def find_invalid_xmas_number(xmas: list, preamble_size: int):
    for i in range(len(xmas) - preamble_size):
        index = i + preamble_size + 1
        target = xmas[index]
        window = xmas[index - preamble_size:index]

        if not has_sum_pair(target, window):
            return target, index

    return False


def find_xmas_encryption_weakness(xmas, target, max_index):
    for i in range(max_index):
        total = xmas[i]
        minimum = xmas[i]
        maximum = xmas[i]
        j = i + 1

        while total < target and j < len(xmas):
            total = total + xmas[j]
            minimum = minimum if minimum < xmas[j] else xmas[j]
            maximum = maximum if maximum > xmas[j] else xmas[j]
            j = j + 1

        if total == target:
            return minimum + maximum


if __name__ == '__main__':
    xmas = [int(i.replace('\n', '')) for i in open('./input.txt').readlines()]
    invalid, index = find_invalid_xmas_number(xmas, 25)
    print('Part 1', invalid)
    print('Part 2', find_xmas_encryption_weakness(xmas, invalid, index))
