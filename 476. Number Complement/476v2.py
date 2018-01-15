class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ ((1 << num.bit_length()) - 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findComplement(5))
