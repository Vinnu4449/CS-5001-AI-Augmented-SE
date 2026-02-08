# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    """
    Calculate the maximum sum for a given integer n using a dynamic programming approach.
    The sum for each number i is the maximum of:
    - i itself
    - the sum of the values at i/2, i/3, i/4, and i/5 (using integer division)

    Args:
        n: The integer for which to compute the maximum sum

    Returns:
        The maximum sum for the given n
    """
    # Initialize the result list with base cases
    res = [0, 1]  # res[0] = 0, res[1] = 1

    # Iterate from 2 to n (inclusive)
    i = 2
    while i < n + 1:
        # Calculate the maximum sum for current i
        current_max = max(
            i,
            res[int(i / 2)] + res[int(i / 3)] + res[int(i / 4)] + res[int(i / 5)]
        )
        res.append(current_max)
        i = i + 1

    return res[n]
```

- Preserved exact function name and signature
- Maintained original algorithm and control flow
- Kept all numeric operations identical (integer division, max calculation)
- Preserved early-exit behavior (none in this case)
- Added docstring explaining the function's purpose
- Improved variable naming for clarity (current_max)
- Maintained original list initialization and growth pattern
- Preserved all return value behavior
- Kept identical loop structure and condition boundaries
- Maintained exact same parameter handling and return type
