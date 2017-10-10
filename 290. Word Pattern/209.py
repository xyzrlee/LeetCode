class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        map = {}
        strList = str.split()
        if len(pattern) != len(strList):
            return False
        for i in range(len(pattern)):
            if pattern[i] in map.keys():
                if map[pattern[i]] != strList[i]:
                    return False
            else:
                if strList[i] in map.values():
                    return False
                map[pattern[i]] = strList[i]
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern('abba', 'dog dog dog dog'))
