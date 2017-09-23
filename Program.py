"""Entry program for Stock Data Processing"""
from CurrConverter import CurrConverter
from CsvIO import read_stock_csv, write_stock_csv

def run():
    """Entry method for Stock Data Processing"""
    stocks = read_stock_csv('AAPL.csv')
    for stock in stocks:
        CurrConverter(.7578).convert_prices(stock)
    write_stock_csv('dict.csv', stocks)

run()
