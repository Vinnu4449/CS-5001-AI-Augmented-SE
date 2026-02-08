def remove_elements(list1, list2):
    """
    Returns a new list containing elements from list1 that are not present in list2.
    Preserves the original order of elements from list1.

    Args:
        list1: The source list to filter elements from
        list2: The list of elements to exclude from list1

    Returns:
        A new list with elements from list1 that don't appear in list2
    """
    result = [x for x in list1 if x not in list2]
    return result
