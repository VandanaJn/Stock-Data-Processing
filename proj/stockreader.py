import csv
from proj import stock


def readstockcsv(fname):
    """readstockcsv returns list of stocks from csv"""
    stocks = []
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stocks.append(stock.stock(row['Date'], row['Open'], row['High'],
                                      row['Low'], row['Close'], row['Adj Close'], row['Volume']))
        return stocks
