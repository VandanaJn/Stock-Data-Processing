"""module to define CsvIO"""
import csv

def read_stock_csv(fname):
    """read_stock_csv reads csv file fname and returns an array of OrderedDict"""
    stocks = []
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stocks.append(row)
        return stocks

def write_stock_csv(fname, items):
    """write_stock_csv creates csv file with fname and writes items to it"""
    with open(fname, 'w') as csv_file:
        if(len(items)> 0):
            writer = csv.DictWriter(
                csv_file, lineterminator='\n', fieldnames=items[0].keys())
            writer.writeheader()
            for item in items:
                writer.writerow(item)
