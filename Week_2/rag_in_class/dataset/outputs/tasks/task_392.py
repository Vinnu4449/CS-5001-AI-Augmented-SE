def get_max_sum(n):
    """
    Calculate the maximum sum for a given integer n using a dynamic programming approach.
    The sum for each number i is the maximum of:
    - i itself
    - the sum of the values at i/2, i/3, i/4, and i/5 (using integer division)

    Args:
        n: The integer for which to compute the maximum sum

    Returns:
        The maximum sum for the given n
    """
    # Initialize the result list with base cases
    res = [0, 1]  # res[0] = 0, res[1] = 1

    # Iterate from 2 to n (inclusive)
    i = 2
    while i < n + 1:
        # Calculate the maximum sum for current i
        current_max = max(
            i,
            res[int(i / 2)] + res[int(i / 3)] + res[int(i / 4)] + res[int(i / 5)]
        )
        res.append(current_max)
        i = i + 1

    return res[n]
