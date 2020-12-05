import re


def get_seat_row(seat: str) -> int:
    return int(seat.replace('F', '0').replace('B', '1')[0:7], 2)


def get_seat_column(seat: str) -> int:
    return int(seat.replace('R', '1').replace('L', '0')[7:10], 2)


def get_seat_id(seat: str) -> int:
    return get_seat_row(seat) * 8 + get_seat_column(seat)


def find_seat(seats):
    seats.sort()

    for i, seat in enumerate(seats):
        target = i + min(seats)

        if target != seat:
            return target


if __name__ == '__main__':
    file = open('./input.txt')
    seats = [get_seat_id(seat) for seat in re.findall(r'\w+', file.read())]
    print('Part 1', max(seats))
    print('Part 2', find_seat(seats))
