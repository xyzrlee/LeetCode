import copy
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if (0 == len(board)): return
        ori, l, r = copy.deepcopy(board), len(board), len(board[0])
        for i in range(l):
            for j in range(r):
                live = self.count(ori, i, j)
                if ori[i][j] == 1 and live < 2:
                    board[i][j] = 0
                elif ori[i][j] == 1 and live > 3:
                    board[i][j] = 0
                elif ori[i][j] == 0 and live == 3:
                    board[i][j] = 1

    def count(self, board: List[List[int]], x, y) -> int:
        c = 0
        for i in (x - 1, x, x + 1):
            if (i < 0 or i >= len(board)):
                continue
            for j in (y - 1, y, y + 1):
                if (j < 0 or j >= len(board[x])):
                    continue
                if (i == x and j == y):
                    continue
                c += board[i][j]
        return c


if __name__ == '__main__':
    a = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    sol = Solution()
    sol.gameOfLife(a)
    print(a)
