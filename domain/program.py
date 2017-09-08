"""Entry program for Stock Data Processing"""
import os
from context import stockreader

FOLDER = os.path.dirname(__file__)
STOCKS = stockreader.readstockcsv(os.path.join(FOLDER, '../datafiles/AAPL.csv'))
for it in STOCKS:
    print(it.dt)
