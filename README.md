# Stock-Data-Processing
Project to Read Apple Stock Prices from csv file and convert prices from dollar to Euros and generate csv file.
It is developed in python 3. This is based on learing python Third assignment -- Data processing pipeline from https://github.com/KevinKershaw/Learn-Python

Sample Run
PS C:\python programs\Stock-Data-Processing> python FileCsvProcessor.py AAPL.csv AAPL_R.csv roman
Number of arguments: 4
Argument List: ['FileCsvProcessor.py', 'AAPL.csv', 'AAPL_R.csv', 'roman']

PS C:\python programs\Stock-Data-Processing> python FileCsvProcessor.py AAPL.csv AAPL_P.csv pound
Number of arguments: 4
Argument List: ['FileCsvProcessor.py', 'AAPL.csv', 'AAPL_P.csv', 'pound']

PS C:\python programs\Stock-Data-Processing> python ConsoleCsvWriter.py | python ConsoleCsvProcessor.py
Date,Open,High,Low,Close,Adj Close,Volume
2016-08-01,79.1219010312,81.5771715156,78.8112,81.4483462734,79.91791688520001,170149200
PS C:\python programs\Stock-Data-Processing>
