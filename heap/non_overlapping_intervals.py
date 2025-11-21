# https://leetcode.com/problems/non-overlapping-intervals/description/
from typing import List
import heapq

class Solution:



    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 最大线段重合长度
        intervals.sort(key=lambda x: x[0])
        ans = 0
        minheap = []

        for interval in intervals:
            while minheap and minheap[0] <= interval[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, interval[1])
            ans = max(ans, len(minheap))

        return ans

s = Solution()
# 1
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
# 2
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
# 0
print(s.eraseOverlapIntervals([[1,2],[3,4]]))