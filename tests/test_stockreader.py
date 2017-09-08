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
        self.assertEqual('2016-08-01', stocks[0].dt)

if __name__ == '__main__':
    unittest.main(exit=False)
    