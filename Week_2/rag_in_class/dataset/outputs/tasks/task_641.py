def is_nonagonal(n):
    """
    Calculate the nth nonagonal number.

    The nth nonagonal number is given by the formula: n * (7n - 5) / 2

    Args:
        n: The index of the nonagonal number to calculate (1-based)

    Returns:
        The nth nonagonal number as an integer
    """
    return int(n * (7 * n - 5) / 2)
