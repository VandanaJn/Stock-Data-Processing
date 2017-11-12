"""Entry program for Stock Data Processing from console"""
from CurrConvert import convert_prices
from CsvIO import read_stock_csv_console, write_stock_csv_console

STOCKS = read_stock_csv_console()
EXCHANGE = .7578
convert_prices(STOCKS, EXCHANGE)
write_stock_csv_console(STOCKS)
