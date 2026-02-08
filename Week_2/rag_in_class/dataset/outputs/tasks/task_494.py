def binary_to_integer(test_tup):
    """Convert a tuple of binary digits (0s and 1s) to a decimal integer string.

    Args:
        test_tup: A tuple containing binary digits (0s and 1s).

    Returns:
        A string representation of the decimal integer formed by the binary digits.
    """
    res = int("".join(str(ele) for ele in test_tup), 2)
    return str(res)
