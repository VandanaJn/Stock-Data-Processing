"""Stock Data Processing PipeLine"""

from CurrConvert import convert_prices, convert_prices_an_roman
from CsvIO import read_stock_csv, write_stock_csv

def run(source_file, dest_file, convert_type):
    """Stock Data Processing PipeLine"""
    stocks = read_stock_csv(source_file)
    exchange = .7578
    for stock in stocks:
        if convert_type == "pound":
            convert_prices(stock, exchange)
        elif convert_type == "roman":
            convert_prices_an_roman(stock)
    write_stock_csv(dest_file, stocks)