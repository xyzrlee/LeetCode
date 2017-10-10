class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        replaceDict = {}
        for i in range(len(s)):
            if s[i] in replaceDict.keys():
                if t[i] != replaceDict[s[i]]:
                    return False
            else:
                if t[i] in replaceDict.values():
                    return False
                replaceDict[s[i]] = t[i]
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic('ab', 'aa'))
