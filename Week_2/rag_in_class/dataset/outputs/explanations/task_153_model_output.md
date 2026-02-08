# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
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
```

- Preserved exact function name and signature
- Maintained identical calculation logic for vertex coordinates
- Kept same return type (tuple) and structure
- Added docstring explaining purpose and return format
- Preserved all numeric operations exactly as original
- No changes to control flow or early returns
- No changes to parameter meaning or mathematical conventions
- No changes to edge case handling (division by zero would still occur if a=0)
- Formatted for better readability while keeping identical behavior
- Verified that tests expecting tuple return would still pass
