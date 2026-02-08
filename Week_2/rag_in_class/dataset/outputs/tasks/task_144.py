def sum_Pairs(arr, n):
    """
    Calculate a weighted sum of array elements based on their positions.

    For each element at index i (0-based), the weight is:
    - Positive contribution: i * arr[i]
    - Negative contribution: (n-1-i) * arr[i]
    The total sum is the sum of all these weighted contributions.

    Args:
        arr: List of numbers to process
        n: Number of elements to consider (must be <= len(arr))

    Returns:
        The computed weighted sum
    """
    sum = 0
    for i in range(n - 1, -1, -1):
        sum += i * arr[i] - (n - 1 - i) * arr[i]
    return sum
