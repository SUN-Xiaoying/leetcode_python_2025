#
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
#
from collections import deque
from typing import Optional, List

from bst.bt_utils import TreeNode, build_tree_from_list, tree_to_array


class Solution:
    #   0ms Beats 100.00%
    #   弹出x
    #   有左加左，有右加右
    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque() # 现在是队列
        result = []
        tree_map = {}
        level=0 # python don't need it ?

        if root:
            queue.append(root)
            tree_map[root] = level
            while queue:
                #   弹出x
                node = queue.popleft()
                level = tree_map[node]
                if len(result) <= level:
                    result.append([])
                result[level].append(node.val)
                #   有左加左
                if node.left:
                    queue.append(node.left)
                    tree_map[node.left] = level+1
                #   有右加右
                if node.right:
                    queue.append(node.right)
                    tree_map[node.right] = level+1

        return result

    def levelOrder_neetcode(self, root: Optional[TreeNode]) -> List[List[int]]:
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
    tree = build_tree_from_list([3,9,20,None,None,15,7])
    # tree = build_tree_from_list([1,2])
    print(sol.levelOrder1(tree))
