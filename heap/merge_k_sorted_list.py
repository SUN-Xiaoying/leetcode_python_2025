# https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=problem-list-v2&envId=heap-priority-queue
# Hard
from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 不是我写的，需要返工
    # 9ms Beats 69.39%
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        head = ListNode(0)
        # 头部生成小根堆
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minheap, (node.val, i, node))  # (val, index, node)

        dummy = ListNode(0)
        current = dummy

        while minheap:
            val, i, node = heapq.heappop(minheap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(minheap, (node.next.val, i, node.next))

        return dummy.next

def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

# Helper: Convert linked list to Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Create input: list of linked lists
input_lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = [build_linked_list(lst) for lst in input_lists]


s = Solution()
# [1,1,2,3,4,4,5,6]
merged = s.mergeKLists(linked_lists)

