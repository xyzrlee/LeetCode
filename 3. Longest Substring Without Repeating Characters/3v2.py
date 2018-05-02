class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        max = -1
        for p, c in enumerate(s):
            l = 0
            if c in pos:
                l = pos[c]
            if max < p - l + 1:
                max = p - l + 1
            pos[c] = p
        return max


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcabcbb'))
