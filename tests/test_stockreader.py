'''test class'''
import unittest
import os
from context import stockreader

class TestStockReader(unittest.TestCase):
    """test_stockreader - Tests stock reader"""

    def test_readstockcsv(self):
        """test_readstockcsv - should read stocks list from csv file """
        folder = os.path.dirname(__file__)
        stocks = stockreader.readstockcsv(os.path.join(folder, '../datafiles/AAPL.csv'))
        self.assertEqual(53, len(stocks))
        self.assertEqual('2016-08-01', stocks[0].dt)
        self.assertEqual(104.410004, stocks[0].open)
        self.assertEqual(107.650002, stocks[0].high)
        self.assertEqual(104.000000, stocks[0].low)
        self.assertEqual(107.480003, stocks[0].close)
        self.assertEqual(105.460434, stocks[0].adjClose)
        self.assertEqual(170149200, stocks[0].volume)

if __name__ == '__main__':
    unittest.main(exit=False)
    