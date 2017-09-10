import csv
from domain import Stock


def readstockcsv(fname):
    """readstockcsv returns list of stocks from csv"""
    stocks = []
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stocks.append(Stock.Stock(row['Date'], float(row['Open']), float(row['High']),
                                      float(row['Low']), float(row['Close']), 
                                      float(row['Adj Close']), int(row['Volume'])))
        return stocks
    