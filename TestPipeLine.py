'''test class'''
import unittest
from unittest.mock import patch, Mock, call
import collections
from PipeLine import run


class TestPipeLine(unittest.TestCase):
    """TestProgram - Tests PipeLine"""

    @patch('PipeLine.convert_prices_an_roman')
    @patch('PipeLine.convert_prices')
    @patch('PipeLine.write_stock_csv')
    @patch('PipeLine.read_stock_csv')
    def test_run(self, mock_readcsv, mock_writecsv, mock_convert_prices, mock_convert_prices_an):
        '''tests run method for pound conversion'''
        mock_parent = Mock()
        mock_parent.attach_mock(mock_readcsv, 'a')
        mock_parent.attach_mock(mock_writecsv, 'b')
        mock_parent.attach_mock(mock_convert_prices, 'c')
        mock_parent.attach_mock(mock_convert_prices_an, 'd')
        obj1 = collections.OrderedDict(
            [('a', 'A1'), ('b', 'B1'), ('c', 'C1')])
        obj2 = collections.OrderedDict(
            [('a', 'A2'), ('b', 'B2'), ('c', 'C2')])
        objects1 = [obj1, obj2]
        mock_readcsv.return_value = objects1
        run('source', 'dest', 'pound')
        mock_convert_prices_an.assert_not_called()
        mock_parent.assert_has_calls([call.a('source'), call.c(
            obj1, 0.7578), call.c(obj2, 0.7578), call.b('dest', objects1)])

    @patch('PipeLine.convert_prices_an_roman')
    @patch('PipeLine.convert_prices')
    @patch('PipeLine.write_stock_csv')
    @patch('PipeLine.read_stock_csv')
    def test_run_an(self, mock_readcsv, mock_writecsv, mock_convert_prices, mock_convert_prices_an):
        '''tests run method for roman conversion'''
        mock_parent = Mock()
        mock_parent.attach_mock(mock_readcsv, 'a')
        mock_parent.attach_mock(mock_writecsv, 'b')
        mock_parent.attach_mock(mock_convert_prices, 'c')
        mock_parent.attach_mock(mock_convert_prices_an, 'd')
        obj1 = collections.OrderedDict(
            [('a', 'A1'), ('b', 'B1'), ('c', 'C1')])
        obj2 = collections.OrderedDict(
            [('a', 'A2'), ('b', 'B2'), ('c', 'C2')])
        objects1 = [obj1, obj2]
        mock_readcsv.return_value = objects1
        run('source', 'dest', 'roman')
        mock_convert_prices.assert_not_called()
        mock_parent.assert_has_calls([call.a('source'), call.d(
            obj1), call.d(obj2), call.b('dest', objects1)])


if __name__ == '__main__':
    unittest.main(exit=False)
