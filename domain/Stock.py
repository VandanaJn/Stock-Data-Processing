"""file to define Stock"""
class Stock:
    """Class Stock"""
    def __init__(self, dt, opn, high, low, close, adjclose, volume):
        """Initializes Stock"""
        self.date = dt
        self.open = opn
        self.high = high
        self.low = low
        self.close = close
        self.adjclose = adjclose
        self.volume = volume
