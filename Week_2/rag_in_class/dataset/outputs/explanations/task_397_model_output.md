# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a, b, c):
    """
    Returns the median value among three numbers a, b, and c.

    The median is the middle value when the three numbers are sorted in ascending order.
    This function uses a series of comparisons to determine the median without sorting.

    Args:
        a (int/float): First number
        b (int/float): Second number
        c (int/float): Third number

    Returns:
        int/float: The median value among a, b, and c
    """
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median
```

- Function name `median_numbers` preserved exactly as in original
- Parameter names `a`, `b`, `c` kept identical to maintain interface
- Return type (int/float) unchanged from original
- All comparison logic preserved exactly (>, <, >=, <=)
- Control flow structure identical (same if/elif/else nesting)
- Early returns not present in original, so none added
- No changes to numeric behavior or comparison semantics
- Added docstring explaining purpose and behavior
- Formatted for better readability with consistent indentation
- Local variable `median` name preserved
- All edge cases handled identically to original (works with any numeric types)
- No new dependencies or helper functions introduced
