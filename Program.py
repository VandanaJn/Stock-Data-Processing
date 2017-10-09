"""Entry program for Stock Data Processing"""
import sys
from CurrConvert import convert_prices, convert_prices_an_roman
from CsvIO import read_stock_csv, write_stock_csv

def run(source_file, dest_file, convert_type):
    """Entry method for Stock Data Processing"""
    stocks = read_stock_csv(source_file)
    exchange = .7578
    for stock in stocks:
        if convert_type == "pound":
            convert_prices(stock, exchange)
        elif convert_type == "roman":
            convert_prices_an_roman(stock)
    write_stock_csv(dest_file, stocks)

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
run(sys.argv[1], sys.argv[2], sys.argv[3])