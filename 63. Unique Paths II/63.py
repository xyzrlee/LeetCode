class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rslt = []
        for i in range(len(obstacleGrid)):
            r = []
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    r.append(0)
                elif i == 0 and j == 0:
                    r.append(1)
                elif i == 0:
                    r.append(r[j-1])
                elif j == 0:
                    r.append(rslt[i-1][j])
                else:
                    r.append(r[j - 1] + rslt[i - 1][j])
            rslt.append(r)
        return rslt[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
