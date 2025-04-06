import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from roman_converter import decimal_to_roman

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

    def test_error(self):
        self.assertRaises(ValueError, decimal_to_roman, 0)
        self.assertRaises(ValueError, decimal_to_roman, 4000)

if __name__ == '__main__':
    unittest.main()