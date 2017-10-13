"""Entry program for Stock Data Processing"""
import sys
from PipeLine import run

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
run(sys.argv[1], sys.argv[2], sys.argv[3])
