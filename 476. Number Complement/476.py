import math


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = ~num
        if result < 0:
            result = result + int(math.pow(2, math.ceil(math.log2(-result))))
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findComplement(1))
