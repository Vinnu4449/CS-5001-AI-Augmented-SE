def parallel_lines(line1, line2):
    """
    Check if two lines are parallel by comparing their slopes.

    Args:
        line1: A tuple (m1, b1) representing the line equation y = m1*x + b1
        line2: A tuple (m2, b2) representing the line equation y = m2*x + b2

    Returns:
        bool: True if the lines are parallel (slopes are equal), False otherwise
    """
    return line1[0] / line1[1] == line2[0] / line2[1]
