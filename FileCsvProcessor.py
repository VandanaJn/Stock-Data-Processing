"""Entry program for Stock Data Processing from and to file"""
import sys
from PipeLine import run

#Usage: Python Program <source_file>, <dest_file>, <convert_type>
#   where source_file is the csv file with stocks data, dest_file is the output csv file
#   convert_type for currency possible values pound|roman

print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))
run(sys.argv[1], sys.argv[2], sys.argv[3])
