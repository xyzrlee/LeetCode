# time limit excceded
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        isPalindrome = []
        result = ''
        for i in range(len(s) + 1):
            l = []
            for j in range(len(s) - i + 1):
                if i <= 1:
                    l.append(True)
                elif j + 1 > len(s):
                    l.append(False)
                else:
                    str = s[j:j + i]
                    if str[0] == str[-1]:
                        l.append(isPalindrome[i - 2][j + 1])
                    else:
                        l.append(False)
                if l[-1] == True:
                    result = s[j:j + i]
                # print('i, j, str, rslt: %d, %d, %s, %r' % (i, j, s[j:j + i], l[-1]))
            isPalindrome.append(l)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('babad'))
