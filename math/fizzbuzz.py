# https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/743/
from typing import List


class Solution:
    # Your runtime beats 100.00 % of python3 submissions
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(4))
    print(s.fizzBuzz(15))