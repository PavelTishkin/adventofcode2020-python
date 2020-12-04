import unittest

from day4 import main


class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.input_data = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''.split('\n')

    def test_get_passports_return_correct_count(self):
        actual = len(main.get_passports(self.input_data))
        self.assertEqual(actual, 4)

    def test_get_passports_contains_correct_fields(self):
        actual = main.get_passports(self.input_data)[2]
        self.assertEqual(actual['hcl'], '#ae17e1')
        self.assertEqual(actual['iyr'], '2013')
        self.assertEqual(actual['eyr'], '2024')
        self.assertEqual(actual['ecl'], 'brn')
        self.assertEqual(actual['pid'], '760753108')
        self.assertEqual(actual['byr'], '1931')
        self.assertEqual(actual['hgt'], '179cm')

    def test_is_passport_valid_detects_valid(self):
        actual = main.is_passport_valid(main.get_passports(self.input_data)[0])
        self.assertTrue(actual)
        actual = main.is_passport_valid(main.get_passports(self.input_data)[2])
        self.assertTrue(actual)

    def test_is_passport_valid_detects_invalid(self):
        actual = main.is_passport_valid(main.get_passports(self.input_data)[1])
        self.assertFalse(actual)
        actual = main.is_passport_valid(main.get_passports(self.input_data)[3])
        self.assertFalse(actual)

    def test_is_birth_year_valid(self):
        actual = main.is_birth_year_valid(2002)
        self.assertTrue(actual)
        actual = main.is_birth_year_valid(2003)
        self.assertFalse(actual)

    def test_is_issue_year_valid(self):
        actual = main.is_issue_year_valid(2020)
        self.assertTrue(actual)
        actual = main.is_issue_year_valid(2021)
        self.assertFalse(actual)

    def test_is_expiration_year_valid(self):
        actual = main.is_expiration_year_valid(2030)
        self.assertTrue(actual)
        actual = main.is_expiration_year_valid(2031)
        self.assertFalse(actual)

    def test_is_height_valid(self):
        actual = main.is_height_valid('60in')
        self.assertTrue(actual)
        actual = main.is_height_valid('190cm')
        self.assertTrue(actual)
        actual = main.is_height_valid('190in')
        self.assertFalse(actual)
        actual = main.is_height_valid('190')
        self.assertFalse(actual)

    def test_is_hair_color_valid(self):
        actual = main.is_hair_color_valid("#123abc")
        self.assertTrue(actual)
        actual = main.is_hair_color_valid("#123abz")
        self.assertFalse(actual)
        actual = main.is_hair_color_valid("123abc")
        self.assertFalse(actual)

    def test_is_eye_color_valid(self):
        actual = main.is_eye_color_valid("brn")
        self.assertTrue(actual)
        actual = main.is_eye_color_valid("wat")
        self.assertFalse(actual)

    def test_is_passport_id_valid(self):
        actual = main.is_passport_id_valid("000000001")
        self.assertTrue(actual)
        actual = main.is_passport_id_valid("0123456789")
        self.assertFalse(actual)
