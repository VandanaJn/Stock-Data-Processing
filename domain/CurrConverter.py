"""file to define CurrConverter"""
class CurrConverter:
    """Class to convert currency"""
    def __init__(self, exchange):
        """Initialize CurrConverter with exchange"""
        self.exchange = exchange

    def convert(self, source):
        """returns converted currency as per exchange rate"""
        return source * self.exchange
