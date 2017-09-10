"""Entry program for Stock Data Processing"""
import os
from context import StockReader

FOLDER = os.path.dirname(__file__)
STOCKS = StockReader.readstockcsv(os.path.join(FOLDER, '../datafiles/AAPL.csv'))
for item in STOCKS:
    print(item.date)
