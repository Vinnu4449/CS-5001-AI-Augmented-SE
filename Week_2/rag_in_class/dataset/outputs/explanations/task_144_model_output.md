# Model output for task_144

## Model
- devstral-small-2:24b-cloud

## Original Code:

def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

## Refactored Code:

```python
def sum_Pairs(arr, n):
    """
    Calculate a weighted sum of array elements based on their positions.

    For each element at index i (0-based), the weight is:
    - Positive contribution: i * arr[i]
    - Negative contribution: (n-1-i) * arr[i]
    The total sum is the sum of all these weighted contributions.

    Args:
        arr: List of numbers to process
        n: Number of elements to consider (must be <= len(arr))

    Returns:
        The computed weighted sum
    """
    sum = 0
    for i in range(n - 1, -1, -1):
        sum += i * arr[i] - (n - 1 - i) * arr[i]
    return sum
```

- Preserved exact function signature and behavior
- Added docstring explaining the weighted sum calculation
- Maintained original loop structure and iteration direction
- Kept identical arithmetic operations and variable names
- Preserved return value type and behavior
- No changes to control flow or early exits
- Formatted for better readability while keeping logic identical
- Verified that the weighted sum formula remains unchanged
- Confirmed that the reverse iteration (n-1 to 0) is preserved
- Maintained exact same parameter semantics (0-based indexing, n as count)
