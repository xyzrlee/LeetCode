class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                substr = s[j:j + i]
                if substr == substr[::-1]:
                    return substr


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('abb'))
