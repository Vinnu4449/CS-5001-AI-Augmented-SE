# Model output for task_558

## Model
- devstral-small-2:24b-cloud

## Original Code:

def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

## Refactored Code:

```python
def digit_distance_nums(n1, n2):
    """Calculate the sum of digits in the absolute difference between two numbers.

    Args:
        n1: First number
        n2: Second number

    Returns:
        Sum of digits in the absolute difference between n1 and n2
    """
    return sum(map(int, str(abs(n1 - n2))))
```

- Preserved exact function name and signature
- Maintained identical behavior for all inputs
- Kept the same control flow (no loops, no branches)
- Preserved the exact calculation: abs(n1-n2) → string → digits → sum
- Maintained return type (int) and return value behavior
- No changes to numeric operations or comparison semantics
- No changes to None handling (not applicable here)
- No changes to early returns (not applicable here)
- Preserved the exact same algorithm and edge-case behavior
- All test assertions will pass unchanged
