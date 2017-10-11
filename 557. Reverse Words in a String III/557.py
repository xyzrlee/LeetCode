class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = s.split()
        rsltList = []
        for i in list:
            rsltList.append(i[::-1])
        return ' '.join(rsltList)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("Let's take LeetCode contest"))
