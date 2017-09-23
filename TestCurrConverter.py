'''test class'''
import unittest
import collections
from CurrConverter import CurrConverter


class TestCurrConverter(unittest.TestCase):
    '''TestCurrConverter - Tests currconverter'''

    def test_convert(self):
        """test_convert - should convert currency as per exchange rate"""
        converter = CurrConverter(.7578)
        self.assertEqual(.7578, converter.convert(1))
        self.assertEqual(1.5156, converter.convert(2))
        self.assertEqual(1.8945, converter.convert(2.5))

    def test_convert_prices(self):
        """test_convert_prices - should convert prices for dictionary object"""
        # Date,Open,High,Low,Close,Adj Close,Volume
        obj1 = collections.OrderedDict(
            [('Date', '2016-08-01'), ('Open', '30'), ('High', '50'), ('Low', '20'),
             ('Close', '25'), ('Adj Close', '30'), ('Volume', '100')])
        converter = CurrConverter(2)
        converter.convert_prices(obj1)
        self.assertEqual('2016-08-01', obj1["Date"])
        self.assertEqual(60, obj1["Open"])
        self.assertEqual(100, obj1["High"])
        self.assertEqual(40, obj1["Low"])
        self.assertEqual(50, obj1["Close"])
        self.assertEqual(60, obj1["Adj Close"])
        self.assertEqual('100', obj1["Volume"])

if __name__ == '__main__':
    unittest.main(exit=False)
