# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
from typing import List

class Solution:
    # Your runtime beats 14.35 % of python3 submissions.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index: int, path:List[int]):
            result.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result

    # TODO: 常看常新
    # Your runtime beats 100.00 % of python3 submissions
    def subsets_neetcode(self,  nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def backtrack(index: int):
            if index >= len(nums):
                return res.append(subsets[:])

            subsets.append(nums[index])
            backtrack(index+1)

            subsets.pop()
            backtrack(index+1)

        backtrack(0)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.subsets_neetcode([1,2,3]))
