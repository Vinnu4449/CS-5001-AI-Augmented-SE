# Model output for task_353

## Model
- devstral-small-2:24b-cloud

## Original Code:

def remove_column(list1, n):
   for i in list1: 
    del i[n] 
   return list1

## Refactored Code:

```python
def remove_column(list1, n):
    """Remove the nth column from each row in the 2D list.

    Args:
        list1: A 2D list where each element is a list representing a row.
        n: The index of the column to remove (0-based).

    Returns:
        The modified 2D list with the specified column removed from each row.
    """
    for i in list1:
        del i[n]
    return list1
```

- Preserved the exact function name `remove_column` and signature
- Maintained the same behavior of modifying each sublist in-place
- Kept the 0-based column index behavior
- Preserved the return of the modified list
- Added a docstring for clarity without changing functionality
- Maintained the same loop structure and deletion operation
- No changes to edge case handling (empty lists, invalid indices would behave the same)
- Preserved the exact control flow and return behavior
