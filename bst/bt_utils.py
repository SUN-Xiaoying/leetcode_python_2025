from collections import deque

# Definition for a binary tree node.
def build_tree_from_list(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    n = len(values)

    while queue and i < n:
        node = queue.popleft()

        # Left child
        if i < n and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < n and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Helper function to build trees (optional, for convenience)
