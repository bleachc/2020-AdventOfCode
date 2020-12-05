import re


def year_validator(minimum: int, maximum: int):
    def validator(x: str):
        match = re.match(r'\b\d{4}\b', x)
        if not match:
            return False
        return minimum <= int(match.group(0)) <= maximum

    return validator


def height_validator(x: str):
    match = re.match(r'(\d{2,3})(cm|in)', x)
    if match:
        val = int(match.group(1))
        units = match.group(2)
        return 150 <= val <= 193 if units == 'cm' else 59 <= val <= 76
    return False


validators = [
    ('byr', year_validator(1920, 2002)),
    ('iyr', year_validator(2010, 2020)),
    ('eyr', year_validator(2020, 2030)),
    ('hgt', height_validator),
    ('hcl', lambda x: re.search(r'#[0-9a-f]{6}\b', x)),
    ('ecl', lambda x: re.search(r'\b(amb|blu|brn|gry|grn|hzl|oth)\b', x)),
    ('pid', lambda x: re.search(r'\b\d{9}\b', x)),
]


def is_valid_passport(passport: dict, validate_values: bool):
    for k, v in validators:
        if k not in passport or (validate_values and not v(passport[k])):
            return False
    return True


if __name__ == '__main__':
    with open('./input.txt') as f:
        passports_txt = [passport.replace('\n', ' ') for passport in f.read().split('\n\n')]
        passports_tuple = [re.findall(r'(\w+):([A-Za-z0-9#]+)', passport) for passport in passports_txt]

        passports = []

        for passport in passports_tuple:
            result = {}
            for key, value in passport:
                result[key] = value
            passports.append(result)

        print('Part 1', len(list(filter(lambda x: is_valid_passport(x, False), passports))))
        print('Part 2', len(list(filter(lambda x: is_valid_passport(x, True), passports))))
