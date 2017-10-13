'''test class'''
import unittest
from unittest.mock import patch
import collections

from PipeLine import run


class TestPipeLine(unittest.TestCase):
    """TestProgram - Tests PipeLine"""

    @patch('PipeLine.convert_prices_an_roman')
    @patch('PipeLine.convert_prices')
    @patch('PipeLine.write_stock_csv')
    @patch('PipeLine.read_stock_csv')
    def test_run(self, mock_readcsv, mock_writecsv, mock_convert_prices, mock_convert_prices_an):
        obj1 = collections.OrderedDict(
            [('a', 'A1'), ('b', 'B1'), ('c', 'C1')])
        obj2 = collections.OrderedDict(
            [('a', 'A1'), ('b', 'B1'), ('c', 'C1')])
        objects1 = [obj1, obj2]
        mock_readcsv.return_value = objects1
        run('source', 'dest', 'pound')
        mock_readcsv.assert_called_with('source')
        mock_convert_prices.assert_called_with(obj1, 0.7578)
        mock_convert_prices.assert_called_with(obj2, 0.7578)
        mock_writecsv.assert_called_with('dest', objects1)
        mock_convert_prices_an.assert_not_called()

    @patch('PipeLine.convert_prices_an_roman')
    @patch('PipeLine.convert_prices')
    @patch('PipeLine.write_stock_csv')
    @patch('PipeLine.read_stock_csv')
    def test_run_an(self, mock_readcsv, mock_writecsv, mock_convert_prices, mock_convert_prices_an):
        obj1 = collections.OrderedDict(
            [('a', 'A1'), ('b', 'B1'), ('c', 'C1')])
        obj2 = collections.OrderedDict(
            [('a', 'A1'), ('b', 'B1'), ('c', 'C1')])
        objects1 = [obj1, obj2]
        mock_readcsv.return_value = objects1
        run('source', 'dest', 'roman')
        mock_readcsv.assert_called_with('source')
        mock_convert_prices_an.assert_called_with(obj1)
        mock_convert_prices_an.assert_called_with(obj2)
        mock_writecsv.assert_called_with('dest', objects1)
        mock_convert_prices.assert_not_called()

if __name__ == '__main__':
    unittest.main(exit=False)
