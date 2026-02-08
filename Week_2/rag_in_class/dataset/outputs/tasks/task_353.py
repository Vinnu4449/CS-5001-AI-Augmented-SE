def remove_column(list1, n):
    """Remove the nth column from each row in the 2D list.

    Args:
        list1: A 2D list where each element is a list representing a row.
        n: The index of the column to remove (0-based).

    Returns:
        The modified 2D list with the specified column removed from each row.
    """
    for i in list1:
        del i[n]
    return list1
