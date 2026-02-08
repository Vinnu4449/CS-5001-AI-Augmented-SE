import math

def area_pentagon(a):
    """
    Calculate the area of a regular pentagon with side length 'a'.

    The formula used is:
    area = (sqrt(5*(5 + 2*sqrt(5))) * a^2) / 4

    Args:
        a (float): The length of a side of the regular pentagon

    Returns:
        float: The area of the pentagon
    """
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
