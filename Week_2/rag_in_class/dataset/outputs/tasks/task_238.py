def number_of_substrings(str):
    """Calculate the number of possible substrings in a given string.

    The number of substrings in a string of length n is given by the formula:
    n * (n + 1) / 2, which is the sum of the first n natural numbers.

    Args:
        str: The input string whose substrings are to be counted.

    Returns:
        int: The number of possible substrings in the input string.
    """
    str_len = len(str)
    return int(str_len * (str_len + 1) / 2)
