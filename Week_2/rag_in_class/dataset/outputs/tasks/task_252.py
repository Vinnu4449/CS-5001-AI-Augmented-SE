import cmath

def convert(numbers):
    """Convert a complex number to its polar form (magnitude, phase in radians).

    Args:
        numbers: A complex number (or iterable of complex numbers)

    Returns:
        The polar form(s) as (magnitude, phase) tuple(s)
    """
    num = cmath.polar(numbers)
    return num
