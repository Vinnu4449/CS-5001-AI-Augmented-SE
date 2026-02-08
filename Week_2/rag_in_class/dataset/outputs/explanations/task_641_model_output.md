# Model output for task_641

## Model
- devstral-small-2:24b-cloud

## Original Code:

def is_nonagonal(n): 
	return int(n * (7 * n - 5) / 2) 

## Refactored Code:

```python
def is_nonagonal(n):
    """
    Calculate the nth nonagonal number.

    The nth nonagonal number is given by the formula: n * (7n - 5) / 2

    Args:
        n: The index of the nonagonal number to calculate (1-based)

    Returns:
        The nth nonagonal number as an integer
    """
    return int(n * (7 * n - 5) / 2)
```

- Preserved the exact function name `is_nonagonal` and signature
- Maintained the original formula `n * (7 * n - 5) / 2` exactly
- Kept the integer conversion behavior
- Added a docstring explaining the formula and parameters
- Preserved all numeric behavior including integer division semantics
- No changes to control flow or return behavior
- Formula remains algebraically identical to original
- Parameter meaning (1-based index) preserved
- Return type (int) unchanged
