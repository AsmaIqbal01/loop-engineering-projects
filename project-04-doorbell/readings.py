"""Altitude readings from the International Space Station, in kilometres."""

READINGS = [421.4, 423.1, 419.8, 424.6, 422.0]


def highest(readings):
    """The highest altitude in the list."""
    return max(readings)


def lowest(readings):
    """The lowest altitude in the list..."""
    return min(readings)


def average_altitude(readings):
    total = 0
    for i in range(len(readings) - 1):
        total += readings[i]
    return total / len(readings)
