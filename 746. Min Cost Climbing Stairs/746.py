from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        length = len(cost)
        if length < 2: return 0
        x, y = cost[0], cost[1]
        for i in range(2, length):
            x, y = y, min(x, y) + cost[i]
        return min(x, y)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(sol.minCostClimbingStairs([0, 0, 0, 1]))
