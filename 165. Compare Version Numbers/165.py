class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        len1 = len(v1)
        len2 = len(v2)
        print(len1, len2)
        for i in range(min(len1, len2)):
            if v1[i] != v2[i]:
                i1 = int(v1[i])
                i2 = int(v2[i])
                if i1 == i2:
                    continue
                if i1 < i2:
                    return -1
                else:
                    return 1
        if len1 > len2:
            return 1
        elif len1 < len2:
            return -1
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.compareVersion('01', '1'))
