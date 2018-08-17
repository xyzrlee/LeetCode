class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        x, y = 0, 0
        if len(s) == 0: return 0
        if s[0] != "0": y = 1
        for i in range(len(s)):
            z = 0
            if s[i] != "0":
                z += y
            if i > 0 and s[i - 1] != "0" and s[i - 1:i + 1] <= "26":
                z += x
            x, y = y, z
        return y


if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings("227"))
