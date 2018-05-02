class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j].find(s[j]) >= 0: break
                if j - i + 1 > maxLength:
                    maxLength = j - i + 1
        return maxLength


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('pwwkew'))
