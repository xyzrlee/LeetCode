class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n = 1
        max = 10 ** (len(str(N)) + 1)
        z = ''.join(sorted([x for x in str(N)]))
        while n <= max:
            s = ''.join(sorted([x for x in str(n)]))
            if s == z: return True
            n *= 2
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.reorderedPowerOf2(46))
