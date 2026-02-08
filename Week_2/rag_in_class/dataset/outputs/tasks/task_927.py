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
