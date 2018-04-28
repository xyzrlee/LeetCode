class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        flag = [True] * n
        flag[0] = flag[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if flag[i]:
                j = i + i
                while j < n:
                    flag[j] = False
                    j += i
        return sum(flag)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(20))
