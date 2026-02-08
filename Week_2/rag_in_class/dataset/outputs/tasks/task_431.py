def common_element(list1, list2):
    """Check if there is any common element between two lists.

    Returns:
        bool: True if there is at least one common element, False otherwise.
    """
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
