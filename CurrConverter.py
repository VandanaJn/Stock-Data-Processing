"""module to define CurrConverter"""

class CurrConverter:
    """Class to convert currency"""

    def __init__(self, exchange):
        """Initialize CurrConverter with exchange"""
        self.exchange = exchange

    def convert(self, source):
        """returns converted currency as per exchange rate"""
        return source * self.exchange

    def convert_prices(self, obj: dict):
        """converts curreny values as per exchange rates in Dict object"""
        obj['Open'] = self.convert(float(obj['Open']))
        obj['High'] = self.convert(float(obj['High']))
        obj['Low'] = self.convert(float(obj['Low']))
        obj['Close'] = self.convert(float(obj['Close']))
        obj['Adj Close'] = self.convert(float(obj['Adj Close']))
