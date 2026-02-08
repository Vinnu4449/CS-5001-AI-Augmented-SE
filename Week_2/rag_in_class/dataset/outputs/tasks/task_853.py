import math

def sum_of_odd_Factors(n):
    """
    Calculate the sum of odd factors of a given integer n.

    This function computes the sum of all odd factors of n by:
    1. Removing all factors of 2 (even factors)
    2. For each odd factor i, calculate the sum of its powers in the factorization
    3. Multiply these sums together to get the total sum of odd factors

    Args:
        n (int): The input integer to find odd factors for

    Returns:
        int: The sum of all odd factors of n
    """
    res = 1
    # Remove all factors of 2 (even factors)
    while n % 2 == 0:
        n = n // 2

    # Check odd factors from 3 up to sqrt(n)
    for i in range(3, int(math.sqrt(n) + 1)):
        count = 0
        curr_sum = 1  # Start with 1 (i^0)
        curr_term = 1  # Current term in geometric series

        # Factor out all occurrences of i
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i  # i^1, i^2, i^3, etc.
            curr_sum += curr_term  # Sum of geometric series: 1 + i + i^2 + ... + i^count

        res *= curr_sum

    # If remaining n is a prime > 2, add (1 + n) to the result
    if n >= 2:
        res *= (1 + n)

    return res
