"""module to define RomanConvert"""

def convert(currency, exchange):
    """returns converted currency as per exchange rate"""
    return currency * exchange

def int_to_roman(val):
    """ Convert an integer to a Roman numeral, borrowed from python-cookbook."""
    if not isinstance(val, type(1)):
        raise TypeError("expected integer")
    if not 0 < val < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC',
            'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(val / ints[i])
        result.append(nums[i] * count)
        val -= ints[i] * count
    return ''.join(result)

def dollar_to_ancient_roman(val):
    """dollar_to_ancient_roman converts a dollar to ancient romans."""
    cents = int(val * 100)
    rocks = cents // 100
    pebbles = int(cents % 100 / 10)
    rock_format = ''
    if rocks > 0:
        rock_format = int_to_roman(rocks)
    else:
        rock_format = "NO"
    if pebbles > 0:
        no_pebbles = int_to_roman(pebbles)
        return "{noRocks} rocks and {0} pebbles".format(no_pebbles, noRocks=rock_format)
    else:
        return "{noRocks} rocks".format(noRocks=rock_format)

def convert_prices(obj: dict, exchange):
    """converts curreny values as per exchange rates in Dict object"""
    obj['Open'] = convert(float(obj['Open']), exchange)
    obj['High'] = convert(float(obj['High']), exchange)
    obj['Low'] = convert(float(obj['Low']), exchange)
    obj['Close'] = convert(float(obj['Close']), exchange)
    obj['Adj Close'] = convert(float(obj['Adj Close']), exchange)

def convert_prices_an_roman(obj: dict):
    """converts curreny values as per exchange rates in Dict object"""
    obj['Open'] = dollar_to_ancient_roman(float(obj['Open']))
    obj['High'] = dollar_to_ancient_roman(float(obj['High']))
    obj['Low'] = dollar_to_ancient_roman(float(obj['Low']))
    obj['Close'] = dollar_to_ancient_roman(float(obj['Close']))
    obj['Adj Close'] = dollar_to_ancient_roman(float(obj['Adj Close']))
