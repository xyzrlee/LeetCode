class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        return str(bin(z)).count("1")


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistance(1, 4))
