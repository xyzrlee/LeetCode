import collections
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def walk(wx: int, wy: int) -> int:
            if wx < 0 or wy < 0: return 0
            if wx >= len(grid): return 0
            if wy >= len(grid[wx]): return 0
            if grid[wx][wy] == 0: return 0
            if x[(wx, wy)] == True: return 0
            x[(wx, wy)] = True
            return walk(wx - 1, wy) + walk(wx, wy - 1) + walk(wx + 1, wy) + walk(wx, wy + 1) + 1

        x = collections.defaultdict(lambda: False)
        m = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                m = max(m, walk(i, j))

        return m


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxAreaOfIsland([[1, 1, 1], [1, 0, 1]]))
    print(sol.maxAreaOfIsland([[1, 1]]))
    print(sol.maxAreaOfIsland([[1, 1], [1, 0]]))
    print(sol.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
