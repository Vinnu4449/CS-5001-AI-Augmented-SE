def parabola_vertex(a, b, c):
    """
    Calculate the vertex of a parabola given coefficients a, b, and c.

    The vertex is returned as a tuple (x, y) where:
    - x is the x-coordinate of the vertex: -b / (2 * a)
    - y is the y-coordinate of the vertex: (4ac - b²) / (4a)

    Args:
        a: Coefficient of x² term (must not be zero)
        b: Coefficient of x term
        c: Constant term

    Returns:
        tuple: (x, y) coordinates of the parabola's vertex
    """
    vertex = (((-b / (2 * a)), (((4 * a * c) - (b * b)) / (4 * a))))
    return vertex
