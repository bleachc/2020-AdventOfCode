import unittest
from .main import validators

byr_validator = validators[0][1]
iyr_validator = validators[1][1]
eyr_validator = validators[2][1]
hgt_validator = validators[3][1]
hcl_validator = validators[4][1]
ecl_validator = validators[5][1]
pid_validator = validators[6][1]


class TestDayFour(unittest.TestCase):
    # BYR

    def test_byr_below_min(self):
        self.assertFalse(byr_validator('1919'))

    def test_byr_at_min(self):
        self.assertTrue(byr_validator('1920'))

    def test_byr_within_range(self):
        self.assertTrue(byr_validator('1950'))

    def test_byr_at_max(self):
        self.assertTrue(byr_validator('2002'))

    def test_byr_above_max(self):
        self.assertFalse(byr_validator('2003'))

    def test_byr_invalid(self):
        self.assertFalse(byr_validator('02002'))

    # IYR

    def test_iyr_below_min(self):
        self.assertFalse(iyr_validator('2009'))

    def test_iyr_at_min(self):
        self.assertTrue(iyr_validator('2010'))

    def test_iyr_within_range(self):
        self.assertTrue(iyr_validator('2015'))

    def test_iyr_at_max(self):
        self.assertTrue(iyr_validator('2020'))

    def test_iyr_above_max(self):
        self.assertFalse(iyr_validator('2021'))

    def test_iyr_invalid(self):
        self.assertFalse(iyr_validator('2020b'))

    # EYR

    def test_eyr_below_min(self):
        self.assertFalse(eyr_validator('2019'))

    def test_eyr_at_min(self):
        self.assertTrue(eyr_validator('2020'))

    def test_eyr_within_range(self):
        self.assertTrue(eyr_validator('2025'))

    def test_eyr_at_max(self):
        self.assertTrue(eyr_validator('2030'))

    def test_eyr_above_max(self):
        self.assertFalse(eyr_validator('2031'))

    def test_eyr_invalid(self):
        self.assertFalse(eyr_validator('a2020'))

    # HGT CM

    def test_hgt_cm_below_min(self):
        self.assertFalse(hgt_validator('149cm'))

    def test_hgt_cm_at_min(self):
        self.assertTrue(hgt_validator('150cm'))

    def test_hgt_cm_within_range(self):
        self.assertTrue(hgt_validator('180cm'))

    def test_hgt_cm_at_max(self):
        self.assertTrue(hgt_validator('193cm'))

    def test_hgt_cm_above_max(self):
        self.assertFalse(hgt_validator('194cm'))

    def test_hgt_cm_invalid(self):
        self.assertFalse(hgt_validator('192'))

    # HGT IN

    def test_hgt_in_below_min(self):
        self.assertFalse(hgt_validator('58in'))

    def test_hgt_cm_in_min(self):
        self.assertTrue(hgt_validator('59in'))

    def test_hgt_in_within_range(self):
        self.assertTrue(hgt_validator('68in'))

    def test_hgt_in_at_max(self):
        self.assertTrue(hgt_validator('76in'))

    def test_hgt_in_above_max(self):
        self.assertFalse(hgt_validator('77in'))

    def test_hgt_in_invalid(self):
        self.assertFalse(hgt_validator('67'))

    # HCL

    def test_hcl_well_formed(self):
        self.assertTrue(hcl_validator('#095adf'))

    def test_hcl_too_long(self):
        self.assertFalse(hcl_validator('#095adff'))

    def test_hcl_too_short(self):
        self.assertFalse(hcl_validator('#95adf'))

    def test_hcl_no_pound(self):
        self.assertFalse(hcl_validator('095adf'))

    def test_hcl_exceed_letter_range(self):
        self.assertFalse(hcl_validator('#095agf'))

    # ECL

    def test_ecl_amb(self):
        self.assertTrue(ecl_validator('amb'))

    def test_ecl_blu(self):
        self.assertTrue(ecl_validator('blu'))

    def test_ecl_brn(self):
        self.assertTrue(ecl_validator('brn'))

    def test_ecl_gry(self):
        self.assertTrue(ecl_validator('gry'))

    def test_ecl_grn(self):
        self.assertTrue(ecl_validator('grn'))

    def test_ecl_hzl(self):
        self.assertTrue(ecl_validator('hzl'))

    def test_ecl_oth(self):
        self.assertTrue(ecl_validator('oth'))

    def test_ecl_contain(self):
        self.assertFalse(ecl_validator('aothr'))

    def test_ecl_begin_amb(self):
        self.assertFalse(ecl_validator('amber'))

    def test_ecl_begin_blu(self):
        self.assertFalse(ecl_validator('blue'))

    def test_ecl_end(self):
        self.assertFalse(ecl_validator('ahzl'))

    # PID

    def test_pid_nine_digits(self):
        self.assertTrue(pid_validator('123456789'))

    def test_pid_nine_characters(self):
        self.assertFalse(pid_validator('abcde6789'))

    def test_pid_ten_digits(self):
        self.assertFalse(pid_validator('1234567890'))

    def test_pid_end_nine_digits(self):
        self.assertFalse(pid_validator('a123456789'))

    def test_pid_begin_nine_digits(self):
        self.assertFalse(pid_validator('123456789a'))


if __name__ == '__main__':
    unittest.main()
