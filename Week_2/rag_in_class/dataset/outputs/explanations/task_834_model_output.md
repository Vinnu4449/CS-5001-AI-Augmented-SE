# Model output for task_834

## Model
- devstral-small-2:24b-cloud

## Original Code:

def generate_matrix(n):
        if n<=0:
            return [] 
        matrix=[row[:] for row in [[0]*n]*n]        
        row_st=0
        row_ed=n-1        
        col_st=0
        col_ed=n-1
        current=1        
        while (True):
            if current>n*n:
                break
            for c in range (col_st, col_ed+1):
                matrix[row_st][c]=current
                current+=1
            row_st+=1
            for r in range (row_st, row_ed+1):
                matrix[r][col_ed]=current
                current+=1
            col_ed-=1
            for c in range (col_ed, col_st-1, -1):
                matrix[row_ed][c]=current
                current+=1
            row_ed-=1
            for r in range (row_ed, row_st-1, -1):
                matrix[r][col_st]=current
                current+=1
            col_st+=1
        return matrix

## Refactored Code:

```python
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
```

- Preserved the exact function signature and behavior of `generate_matrix(n)`
- Maintained the same control flow and loop structures
- Kept the same boundary adjustment logic (row_start, row_end, col_start, col_end)
- Preserved the spiral filling order (right, down, left, up)
- Maintained the same early exit condition (current > n*n)
- Kept the same matrix initialization approach
- Added clear docstring explaining the function's purpose and behavior
- Renamed variables for better readability (e.g., row_st → row_start)
- Preserved all numeric operations and comparison semantics exactly
- Maintained the same return value behavior (empty list for n <= 0)
- Verified that the spiral pattern generation remains identical to the original
