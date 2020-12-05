import unittest
from .main import get_seat_row, get_seat_column, get_seat_id


class TestDayFive(unittest.TestCase):
    def test_get_seat_row_zero(self):
        self.assertEqual(get_seat_row('FFFFFFFRRR'), 0)

    def test_get_seat_row_one_hundred_twenty_seven(self):
        self.assertEqual(get_seat_row('BBBBBBBRRR'), 127)

    def test_get_seat_row_seventy(self):
        self.assertEqual(get_seat_row('BFFFBBFRRR'), 70)

    def test_get_seat_row_fourteen(self):
        self.assertEqual(get_seat_row('FFFBBBFRRR'), 14)

    def test_get_seat_row_one_hundred_two(self):
        self.assertEqual(get_seat_row('BBFFBBFRLL'), 102)

    def test_get_seat_column_zero(self):
        self.assertEqual(get_seat_column('FFFFFFFLLL'), 0)

    def test_get_seat_column_seven(self):
        self.assertEqual(get_seat_column('FFFBBBFRRR'), 7)

    def test_get_seat_row_four(self):
        self.assertEqual(get_seat_column('BBFFBBFRLL'), 4)

    def test_get_seat_id_five_hundred_sixty_seven(self):
        self.assertEqual(get_seat_id('BFFFBBFRRR'), 567)

    def test_get_seat_id_one_hundred_nineteen(self):
        self.assertEqual(get_seat_id('FFFBBBFRRR'), 119)

    def test_get_seat_id_eight_hundred_twenty(self):
        self.assertEqual(get_seat_id('BBFFBBFRLL'), 820)

    def test_example_seat(self):
        self.assertEqual(get_seat_id('FBFBBFFRLR'), 357)

    def test_get_seat_id_zero(self):
        self.assertEqual(get_seat_id('FFFFFFFLLL'), 0)

    def test_get_seat_id_max(self):
        self.assertEqual(get_seat_id('BBBBBBBRRR'), 1023)


if __name__ == '__main__':
    unittest.main()
