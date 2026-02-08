def count_Hexadecimal(L, R):
    """
    Counts the number of hexadecimal digits in the decimal representation of numbers from L to R (inclusive).

    A hexadecimal digit is any digit in the range 10-15 (A-F in hexadecimal).
    For numbers 10-15, they are counted directly as they represent single hexadecimal digits.
    For numbers >15, each digit in their base-16 representation is checked if it's a hexadecimal digit (10-15).

    Args:
        L (int): Start of range (inclusive)
        R (int): End of range (inclusive)

    Returns:
        int: Count of hexadecimal digits found in the range
    """
    count = 0
    for i in range(L, R + 1):
        if (i >= 10 and i <= 15):
            count += 1
        elif (i > 15):
            k = i
            while (k != 0):
                if (k % 16 >= 10):
                    count += 1
                k = k // 16
    return count
