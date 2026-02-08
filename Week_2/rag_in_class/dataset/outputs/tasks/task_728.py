def sum_list(lst1, lst2):
    """Return a new list where each element is the sum of corresponding elements from lst1 and lst2.

    Args:
        lst1: First input list of numbers
        lst2: Second input list of numbers (must be same length as lst1)

    Returns:
        List of sums with same length as inputs
    """
    res_list = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return res_list
