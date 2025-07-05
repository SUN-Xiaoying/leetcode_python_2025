#
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
#
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# You are here!
# Your runtime beats 100.00 % of python3 submissions.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Helper function to build trees (optional, for convenience)
def build_tree_from_list(values):
    """ Builds a binary tree from a list of values (level order), where None indicates a missing node """
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kid_idx = 1
    for idx in range(len(nodes)):
        if nodes[idx] is not None:
            if kid_idx < len(nodes):
                nodes[idx].left = nodes[kid_idx]
                kid_idx += 1
            if kid_idx < len(nodes):
                nodes[idx].right = nodes[kid_idx]
                kid_idx += 1
    return nodes[0]

if __name__ == "__main__":
    sol = Solution()
    tree = build_tree_from_list([1, 2, 3, 4, 5])
    print(sol.maxDepth(tree))
