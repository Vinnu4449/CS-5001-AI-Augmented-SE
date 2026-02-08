def generate_matrix(n):
    """
    Generates an n x n matrix filled with numbers from 1 to n*n in a spiral order.
    The spiral starts from the top-left corner and moves right, then down, then left, then up,
    and repeats this pattern while shrinking the boundaries.

    Args:
        n (int): The size of the matrix (n x n). If n <= 0, returns an empty list.

    Returns:
        list: A 2D list (matrix) filled with numbers in spiral order, or empty list if n <= 0.
    """
    if n <= 0:
        return []
    # Create an n x n matrix initialized with zeros
    matrix = [row[:] for row in [[0] * n] * n]
    # Initialize boundaries
    row_start = 0
    row_end = n - 1
    col_start = 0
    col_end = n - 1
    current = 1  # Starting number

    while True:
        if current > n * n:
            break
        # Fill top row from left to right
        for c in range(col_start, col_end + 1):
            matrix[row_start][c] = current
            current += 1
        row_start += 1
        # Fill right column from top to bottom
        for r in range(row_start, row_end + 1):
            matrix[r][col_end] = current
            current += 1
        col_end -= 1
        # Fill bottom row from right to left
        for c in range(col_end, col_start - 1, -1):
            matrix[row_end][c] = current
            current += 1
        row_end -= 1
        # Fill left column from bottom to top
        for r in range(row_end, row_start - 1, -1):
            matrix[r][col_start] = current
            current += 1
        col_start += 1
    return matrix
