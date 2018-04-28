class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        for i in range(1, l // 2 + 1):
            if l % i == 0:
                j = i
                while j < l:
                    if s[j] != s[j - i]:
                        break
                    j += 1
                else:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern('abababababa'))
