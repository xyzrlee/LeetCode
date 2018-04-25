class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n, r = abs(num), ''
        while n:
            r = str(n % 7) + r
            n //= 7
        r = r.lstrip('0') or '0'
        if num < 0:
            r = '-' + r
        return r


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToBase7(100))
