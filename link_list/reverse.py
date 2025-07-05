# https://leetcode.com/problems/reverse-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 0ms Beats 100.00%

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = None
        temp = head
        after = temp

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        head = before

        return head
