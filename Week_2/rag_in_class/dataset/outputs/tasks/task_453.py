import math

def sumofFactors(n):
    """
    Calculate the sum of factors of n, with special handling for the factor 2.
    Returns 0 if n is odd.
    For even n, computes the product of (1 + i + i^2 + ... + i^k) for each prime factor i^k.
    Special case: when 2 appears exactly once as a factor, the sum for 2 is treated as 0.
    """
    if n % 2 != 0:
        return 0

    res = 1
    # Iterate through potential factors up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0
        curr_sum = 1
        curr_term = 1

        # Count the exponent of current prime factor i
        while n % i == 0:
            count += 1
            n = n // i

            # Special case: if 2 appears exactly once, set its sum contribution to 0
            if i == 2 and count == 1:
                curr_sum = 0

            curr_term *= i
            curr_sum += curr_term

        res *= curr_sum

    # Handle remaining prime factor (if n is still > 1 after loop)
    if n >= 2:
        res *= (1 + n)

    return res
