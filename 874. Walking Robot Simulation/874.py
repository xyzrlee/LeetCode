from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        face = ((0, 1), (-1, 0), (0, -1), (1, 0))
        obs = set(map(tuple, obstacles))
        result, fp, x, y = 0, 0, 0, 0
        for c in commands:
            if c == -2:
                fp = (fp + 1) % 4
            elif c == -1:
                fp = (fp - 1) % 4
            elif 1 <= c <= 9:
                (ax, ay) = face[fp]
                for i in range(c):
                    if (x + ax, y + ay) in obs:
                        break
                    x, y = x + ax, y + ay
            result = max(result, x ** 2 + y ** 2)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.robotSim([7, -2, -2, 7, 5],
                       [[-3, 2], [-2, 1], [0, 1], [-2, 4], [-1, 0], [-2, -3], [0, -3], [4, 4], [-3, 3], [2, 2]]))
    print(sol.robotSim([-2, 8, 3, 7, -1],
                       [[-4, -1], [1, -1], [1, 4], [5, 0], [4, 5], [-2, -1], [2, -5], [5, 1], [-3, -1], [5, -3]]))
