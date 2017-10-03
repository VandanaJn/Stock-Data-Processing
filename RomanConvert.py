"""module to define RomanConvert"""


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
    cents = val * 100
    cents = int(cents)
    rocks = cents // 100
    pebbles = int(cents % 100 / 10)
    rockformat = ''
    if rocks > 0:
        rockformat = int_to_roman(rocks)
    else:
        rockformat = "NO"
    if pebbles > 0:
        return "{0} rocks and {1} pebbles".format(rockformat, int_to_roman(pebbles))
    else:
        return "{0} rocks".format(rockformat)
