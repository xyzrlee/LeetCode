class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s + s)[1:-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern('abababababab'))
