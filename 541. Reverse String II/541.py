class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return s[:k][::-1] + s[k:k * 2] + self.reverseStr(s[k * 2:], k) if s else ''


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseStr('abcdefg', 2))
