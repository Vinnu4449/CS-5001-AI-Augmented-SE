def smallest_Divisor(n):
    """Find the smallest divisor of n greater than 1.

    Args:
        n: Integer to find the smallest divisor for (must be >= 1)

    Returns:
        The smallest divisor of n greater than 1, or n itself if n is prime.
    """
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n
