# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/
from typing import List


class Solution:
    # Your runtime beats 100.00 % of python3 submissions.
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        stack=[]

        def backtrack(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return

            if openN<n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()

            if closeN<openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()

        backtrack(0, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))





