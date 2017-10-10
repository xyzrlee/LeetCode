class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result = True
        replaceDict = {}
        revDict = {}
        for i in range(len(s)):
            if s[i] in replaceDict.keys():
                if t[i] != replaceDict[s[i]]:
                    result = False
                    break
            else:
                if t[i] in revDict.keys():
                    if s[i] != revDict[t[i]]:
                        result = False
                        break
                replaceDict[s[i]] = t[i]
                revDict[t[i]] = s[i]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic('ab', 'aa'))
