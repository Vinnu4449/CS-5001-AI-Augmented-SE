# Model output for task_927

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def max_height(node): 
	if node is None: 
		return 0 ; 
	else : 
		left_height = max_height(node.left) 
		right_height = max_height(node.right) 
		if (left_height > right_height): 
			return left_height+1
		else: 
			return right_height+1

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_height(node):
    """
    Calculate the maximum height of a binary tree.

    Args:
        node: The root node of the binary tree (or None for empty tree)

    Returns:
        int: The maximum height of the tree (0 for empty tree)
    """
    if node is None:
        return 0
    else:
        left_height = max_height(node.left)
        right_height = max_height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
```

- Preserved all function names and signatures exactly as in original
- Maintained identical control flow structure (if/else branches, recursion)
- Kept all return types and values identical (0 for None, +1 for height calculation)
- Preserved the exact comparison logic (left_height > right_height)
- Added docstring for clarity without changing behavior
- Maintained all original variable names and parameter handling
- Kept the same early return for None case
- Preserved the recursive structure and base case exactly
- All numeric operations remain identical (no changes to +1 or comparison)
- No changes to None handling or sentinel values
