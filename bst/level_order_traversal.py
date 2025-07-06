#
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
#
from collections import deque
from typing import Optional, List

from bst.bt_utils import TreeNode, build_tree_from_list, tree_to_array


class Solution:
    def levelOrder_wrong(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        array = tree_to_array(root)
        result: List[List[int]] = []
        temp : List[int] = []
        level = 0
        index = 0
        while index < len(array):
            node_nums = 2 ** level
            while node_nums >0 and index < len(array):
                if array[index] is not None:
                    temp.append(array[index])
                index += 1
                node_nums -= 1
            level += 1
            if temp:
                result.append(temp)
            temp = []

        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            q_len = len(queue)
            level = []
            for _ in range(q_len):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                q_len -= 1
            if level:
                result.append(level)

        return result



if __name__ == "__main__":
    sol = Solution()
    # tree = build_tree_from_list([3,9,20,None,None,15,7])
    tree = build_tree_from_list([1,2])
    print(sol.levelOrder(tree))
