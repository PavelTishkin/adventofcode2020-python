import re


def main():
    input_file = open('input/day4.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))

    passports = get_passports(file_lines)
    valid_passports_count = 0
    valid_passports_fields_count = 0
    for passport in passports:
        if is_passport_valid(passport):
            valid_passports_count += 1
        if is_passport_valid(passport, True):
            valid_passports_fields_count += 1
    print("Answer 1: {}".format(valid_passports_count))
    print("Answer 2: {}".format(valid_passports_fields_count))


def get_passports(input_lines):
    passports = []
    passport = {}
    for i, input_line in enumerate(input_lines):
        input_line = input_line.strip()
        if input_line == "":
            passports.append(passport)
            passport = {}
        else:
            pairs = input_line.split()
            passport.update({pair.split(':')[0]: pair.split(':')[1] for pair in pairs})
            if i == len(input_lines) - 1:
                passports.append(passport)

    return passports


def is_passport_valid(passport, field_check=False):
    keys = passport.keys()
    if ('byr' in keys and 'iyr' in keys and 'eyr' in keys and 'hgt' in keys and 'hcl' in keys and 'ecl' in keys
            and 'pid' in keys):
        if field_check:
            return (is_birth_year_valid(int(passport['byr']))
                    and is_issue_year_valid(int(passport['iyr']))
                    and is_expiration_year_valid(int(passport['eyr']))
                    and is_height_valid(passport['hgt'])
                    and is_hair_color_valid(passport['hcl'])
                    and is_eye_color_valid(passport['ecl'])
                    and is_passport_id_valid(passport['pid']))
        else:
            return True
    return False


def is_birth_year_valid(byr):
    return 1920 <= byr <= 2002


def is_issue_year_valid(byr):
    return 2010 <= byr <= 2020


def is_expiration_year_valid(byr):
    return 2020 <= byr <= 2030


def is_height_valid(height):
    if height.endswith('cm') or height.endswith('in'):
        hgt = int(height[0:len(height) - 2])
    else:
        return False
    if height.endswith('cm'):
        return 150 <= hgt <= 193
    elif height.endswith('in'):
        return 59 <= hgt <= 76
    return True


def is_hair_color_valid(color):
    return re.match('^#[0-9a-f]{6}$', color) is not None


def is_eye_color_valid(color):
    return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_passport_id_valid(pid):
    return re.match('^[0-9]{9}$', pid) is not None


main()
