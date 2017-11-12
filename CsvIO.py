"""module to define CsvIO"""
import csv
import sys

def read_stock_csv(fname):
    """read_stock_csv reads csv file fname and returns an array of OrderedDict"""
    with open(fname) as csvfile:
        return read_stock_csv_stream(csvfile)

def read_stock_csv_stream(stream):
    """read_stock_csv reads csv from stream and returns an array of OrderedDict"""
    stocks = []
    reader = csv.DictReader(stream)
    for row in reader:
        stocks.append(row)
    return stocks

def write_stock_csv(fname, items):
    """write_stock_csv creates csv file with fname and writes items to it"""
    with open(fname, 'w') as csv_file:
        write_stock_csv_stream(items, csv_file)

def write_stock_csv_stream(items, stream):
    """write_stock_csv_console writes items in the dictionary to stream"""
    if len(items) > 0:
        writer = csv.DictWriter(
            stream, lineterminator='\n', fieldnames=items[0].keys())
        writer.writeheader()
        for item in items:
            writer.writerow(item)

def read_stock_csv_console():
    """read_stock_csv reads csv from stdin and returns an array of OrderedDict"""
    return read_stock_csv_stream(sys.stdin)

def write_stock_csv_console(items):
    """write_stock_csv_console writes items in the dictionary to stdout"""
    write_stock_csv_stream(items, sys.stdout)
