'''test class'''
import unittest
import collections
from CsvIO import read_stock_csv, write_stock_csv

class TestCsvIO(unittest.TestCase):
    """TestCsvIO - Tests stock io"""

    def test_readstockcsv(self):
        """test_readstockcsv - should read stocks list from csv file """
        stocks = read_stock_csv('AAPL.csv')
        self.assertEqual(53, len(stocks))
        self.assertEqual('2016-08-01', stocks[0]["Date"])
        self.assertEqual('104.410004', stocks[0]["Open"])
        self.assertEqual('107.650002', stocks[0]["High"])
        self.assertEqual('104.000000', stocks[0]["Low"])
        self.assertEqual('107.480003', stocks[0]["Close"])
        self.assertEqual('105.460434', stocks[0]["Adj Close"])
        self.assertEqual('170149200', stocks[0]["Volume"])

    def test_write_stock_csv(self):
        """test_write_stock_csv - should write stocks list to csv file"""
        obj1 = collections.OrderedDict(
            [('a', 'A1'), ('b', 'B1'), ('c', 'C1')])
        obj2 = collections.OrderedDict(
            [('a', 'A2'), ('b', 'B2'), ('c', 'C2')])
        objects1 = [obj1, obj2]
        write_stock_csv('test.csv', objects1)
        objects2 = read_stock_csv('test.csv')
        self.assertEqual(objects1, objects2)

if __name__ == '__main__':
    unittest.main(exit=False)
