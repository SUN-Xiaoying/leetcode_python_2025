# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Your runtime beats 100.00 % of python3 submissions.
        def backtrack_mine(rest_nums:List[int]) -> List[List[int]]:
            if not rest_nums:
                return [[]]

            result=[]
            for i in range(len(rest_nums)):
                first = rest_nums[i]
                rest = rest_nums[:i] + rest_nums[i + 1:]

                for item in backtrack_mine(rest):
                    result.append([first] + item)

            return result

        return backtrack_mine(nums)

    # TODO: I do not understand
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])  # Copy the current permutation
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                print("Start: ", nums[start], " nums: ", nums)
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo swap)

        backtrack(0)
        return result

if __name__ == '__main__':

    s = Solution()
    print(s.permute([1,2,3]))