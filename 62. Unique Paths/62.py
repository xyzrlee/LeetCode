class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rslt = []
        for i in range(m):
            r = []
            for j in range(n):
                if i == 0:
                    r.append(1)
                elif j == 0:
                    r.append(1)
                else:
                    r.append(r[j - 1] + rslt[i - 1][j])
            rslt.append(r)
        return rslt[m - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(3, 7))
