from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if (0 == len(grid)):
            return 0
        x, y = len(grid), len(grid[0])

        grid2 = list(zip(*grid))
        front, side = [], []
        for x in grid:
            side.append(max(x))
        for x in grid2:
            front.append(max(x))
        sum = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                sum += max(0, min(front[y], side[x]) - grid[x][y])
        return sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
