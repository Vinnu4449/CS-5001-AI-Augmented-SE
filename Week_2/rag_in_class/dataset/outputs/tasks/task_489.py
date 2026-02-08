def frequency_Of_Largest(n, arr):
    """Return the frequency of the largest element in the array.

    Args:
        n: Length of the array (must match len(arr))
        arr: Input array of numbers

    Returns:
        Frequency count of the maximum value in arr
    """
    mn = arr[0]
    freq = 1
    for i in range(1, n):
        if arr[i] > mn:
            mn = arr[i]
            freq = 1
        elif arr[i] == mn:
            freq += 1
    return freq
