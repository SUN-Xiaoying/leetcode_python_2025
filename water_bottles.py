# https://leetcode.com/problems/water-bottles/?envType=daily-question&envId=2025-10-01



class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # 0ms Beats 100.00%
        # TODO: There is a simple solution
        def bfs(fullBottles: int, emptyBottles:int, result:int) -> int:
            if fullBottles == 0 and emptyBottles < numExchange:
                return result
            result += fullBottles
            emptyBottles +=  fullBottles
            fullBottles = emptyBottles // numExchange
            emptyBottles -= fullBottles * numExchange

            result = bfs(fullBottles, emptyBottles, result)
            return result

        return bfs(numBottles, 0, 0)


s = Solution()
# 19
print(s.numWaterBottles(15, 4))
