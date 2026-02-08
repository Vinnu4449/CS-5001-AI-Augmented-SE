# Model output for task_161

## Model
- devstral-small-2:24b-cloud

## Original Code:

def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

## Refactored Code:

```python
def remove_elements(list1, list2):
    """
    Returns a new list containing elements from list1 that are not present in list2.
    Preserves the original order of elements from list1.

    Args:
        list1: The source list to filter elements from
        list2: The list of elements to exclude from list1

    Returns:
        A new list with elements from list1 that don't appear in list2
    """
    result = [x for x in list1 if x not in list2]
    return result
```

- Preserved exact function signature and behavior
- Added clear docstring explaining purpose and parameters
- Maintained original list comprehension logic
- Kept same return type and value
- Preserved order of elements from list1
- No changes to control flow or edge case handling
- No new dependencies or helper functions
- Maintained exact same behavior for empty lists, None values, and all other inputs
- Preserved original comparison semantics (using 'not in' operator)
- No changes to numeric or mathematical behavior
