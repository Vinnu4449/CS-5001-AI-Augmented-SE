def digit_distance_nums(n1, n2):
    """Calculate the sum of digits in the absolute difference between two numbers.

    Args:
        n1: First number
        n2: Second number

    Returns:
        Sum of digits in the absolute difference between n1 and n2
    """
    return sum(map(int, str(abs(n1 - n2))))
