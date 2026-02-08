def median_numbers(a, b, c):
    """
    Returns the median value among three numbers a, b, and c.

    The median is the middle value when the three numbers are sorted in ascending order.
    This function uses a series of comparisons to determine the median without sorting.

    Args:
        a (int/float): First number
        b (int/float): Second number
        c (int/float): Third number

    Returns:
        int/float: The median value among a, b, and c
    """
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median
