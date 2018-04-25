class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        count = bin(n)[2:].count('1')
        if count == 1:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(-16))
