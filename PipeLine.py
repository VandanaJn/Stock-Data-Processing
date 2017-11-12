"""Stock Data Processing PipeLine"""

from CurrConvert import convert_prices, convert_prices_an_roman
from CsvIO import read_stock_csv, write_stock_csv

def run(source_file, dest_file, convert_type):
    """Stock Data Processing PipeLine"""
    stocks = read_stock_csv(source_file)
    if convert_type == "pound":
        convert_prices(stocks, .7578)
    elif convert_type == "roman":
        convert_prices_an_roman(stocks)
    write_stock_csv(dest_file, stocks)
