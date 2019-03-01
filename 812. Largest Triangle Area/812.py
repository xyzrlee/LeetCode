from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def getArea(x: List[int], y: List[int], z: List[int]) -> float:
            s = 0.5 * abs((y[0] - x[0]) * (z[1] - x[1]) - (z[0] - x[0]) * (y[1] - x[1]))
            return s

        m = 0.0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    m = max(m, getArea(points[i], points[j], points[k]))
        return m


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
