# https://leetcode.com/problems/reverse-pairs/description/
# Hard
from typing import List


class Solution:
    # 949ms Beats 34.21%
    def reversePairs(self, nums: List[int]) -> int:
        def counts(left:int, right:int)->int:
            if left==right: return 0
            mid = (left+right) // 2
            return counts(left, mid) + counts(mid+1, right) + merge(left, mid, right)

        def merge(left:int, mid:int, right:int)->int:
            # 统计
            i, j = left, mid + 1
            ans =0
            while i<=mid:
                while j<=right and nums[i]>nums[j]*2:
                    j+=1
                ans += j-mid-1
                i+=1
            # merge
            a, b = left, mid+1
            result=[]
            while a<=mid and b<=right:
                if nums[a] <= nums[b]:
                    result.append(nums[a])
                    a+=1
                else:
                    result.append(nums[b])
                    b+=1
            result.extend(nums[a:mid+1])
            result.extend(nums[b:right+1])
            for i in range(left, right+1):
                nums[i]=result[i-left]
            return ans

        return counts(0, len(nums)-1)

s = Solution()
#3
print(s.reversePairs([2,4,3,5,1]))