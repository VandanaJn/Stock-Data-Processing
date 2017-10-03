'''test class'''
import unittest
from RomanConvert import int_to_roman, dollar_to_ancient_roman


class TestRomanConvert(unittest.TestCase):
    '''TestRomanConvert - Tests RomanConvert'''

    def test_int_to_roman_1_10(self):
        """int_to_roman - tests iputs 1 to 10"""
        self.assertEqual('I', int_to_roman(1))
        self.assertEqual('II', int_to_roman(2))
        self.assertEqual('III', int_to_roman(3))
        self.assertEqual('IV', int_to_roman(4))
        self.assertEqual('V', int_to_roman(5))
        self.assertEqual('VI', int_to_roman(6))
        self.assertEqual('VII', int_to_roman(7))
        self.assertEqual('VIII', int_to_roman(8))
        self.assertEqual('IX', int_to_roman(9))
        self.assertEqual('X', int_to_roman(10))

    def test_int_to_roman_11_20(self):
        """int_to_roman - tests iputs 11 to 20"""
        self.assertEqual('XI', int_to_roman(11))
        self.assertEqual('XII', int_to_roman(12))
        self.assertEqual('XIII', int_to_roman(13))
        self.assertEqual('XIV', int_to_roman(14))
        self.assertEqual('XV', int_to_roman(15))
        self.assertEqual('XVI', int_to_roman(16))
        self.assertEqual('XVII', int_to_roman(17))
        self.assertEqual('XVIII', int_to_roman(18))
        self.assertEqual('XIX', int_to_roman(19))
        self.assertEqual('XX', int_to_roman(20))

    def test_int_to_roman_21_50(self):
        """int_to_roman - tests iputs 21 to 50"""
        self.assertEqual('XXI', int_to_roman(21))
        self.assertEqual('XXX', int_to_roman(30))
        self.assertEqual('XXXII', int_to_roman(32))
        self.assertEqual('XXXIX', int_to_roman(39))
        self.assertEqual('XL', int_to_roman(40))
        self.assertEqual('XLI', int_to_roman(41))
        self.assertEqual('XLIX', int_to_roman(49))
        self.assertEqual('L', int_to_roman(50))

    def test_int_to_roman_51_100(self):
        """int_to_roman - tests iputs 51 to 100"""
        self.assertEqual('LI', int_to_roman(51))
        self.assertEqual('LX', int_to_roman(60))
        self.assertEqual('LXV', int_to_roman(65))
        self.assertEqual('LXX', int_to_roman(70))
        self.assertEqual('LXXIX', int_to_roman(79))
        self.assertEqual('LXXX', int_to_roman(80))
        self.assertEqual('XC', int_to_roman(90))
        self.assertEqual('XCIX', int_to_roman(99))
        self.assertEqual('C', int_to_roman(100))

    def test_int_to_roman_101_4000(self):
        """int_to_roman - tests iputs 51 to 100"""
        self.assertEqual('CI', int_to_roman(101))
        self.assertEqual('CCCXCIX', int_to_roman(399))
        self.assertEqual('CD', int_to_roman(400))
        self.assertEqual('D', int_to_roman(500))
        self.assertEqual('CM', int_to_roman(900))
        self.assertEqual('CMXC', int_to_roman(990))
        self.assertEqual('M', int_to_roman(1000))
        self.assertEqual('MM', int_to_roman(2000))
        self.assertEqual('MMM', int_to_roman(3000))
        self.assertEqual('MMMCMXCIX', int_to_roman(3999))

    def test_dollar_to_ancient_roman(self):
        """test for converting dollar_to_cents with decimal trancation"""

        self.assertEqual('XII rocks', dollar_to_ancient_roman(12.0))
        self.assertEqual('V rocks and VI pebbles',
                         dollar_to_ancient_roman(5.6))
        self.assertEqual('V rocks and VI pebbles',
                         dollar_to_ancient_roman(5.65))
        self.assertEqual('V rocks', dollar_to_ancient_roman(5.06))
        self.assertEqual('NO rocks', dollar_to_ancient_roman(0.0))
        self.assertEqual('NO rocks and V pebbles',
                         dollar_to_ancient_roman(0.5))


if __name__ == '__main__':
    unittest.main(exit=False)
