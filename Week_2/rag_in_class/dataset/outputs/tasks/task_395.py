def first_non_repeating_character(str1):
    """Return the first non-repeating character in the string, or None if all characters repeat.

    Args:
        str1: Input string to search

    Returns:
        The first character that appears exactly once, or None if no such character exists
    """
    # Track the order of first occurrences
    char_order = []
    # Count occurrences of each character
    ctr = {}

    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)

    # Check characters in order of first appearance
    for c in char_order:
        if ctr[c] == 1:
            return c

    return None
