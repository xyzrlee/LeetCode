class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s == "": return [[]]
        if len(s) == 1: return [[s]]
        result = []
        for i in range(len(s)):
            sa = s[:i + 1]
            sb = s[i::-1]
            if sa == sb:
                subpar = self.partition(s[i + 1:])
                for x in subpar:
                    result.append([sa] + x)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.partition("aab"))
