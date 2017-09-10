'''test class'''
import unittest
from context import CurrConverter

class TestCurrConverter(unittest.TestCase):
    '''TestCurrConverter - Tests currconverter'''

    def test_convert(self):
        """test_convert - should convert currency as per exchange rate"""
        converter = CurrConverter.CurrConverter(.7578)
        self.assertEqual(.7578, converter.convert(1))
        self.assertEqual(1.5156, converter.convert(2))
        self.assertEqual(1.8945, converter.convert(2.5))
        

if __name__ == '__main__':
    unittest.main(exit=False)
