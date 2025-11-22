# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
from typing import Optional

from linklist.helper import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
