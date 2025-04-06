import unittest
from roman import decimal_to_roman

class TestRoman(unittest.TestCase):
    def test_roman_basic(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")

    def test_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")

    def test_large(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(409), "CDIX")
        self.assertEqual(decimal_to_roman(909), "CMIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()