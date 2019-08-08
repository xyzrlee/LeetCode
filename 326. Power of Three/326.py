import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        x = math.log10(n) / math.log10(3)
        return x == int(x)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfThree(0))
    print(sol.isPowerOfThree(28))
    print(sol.isPowerOfThree(27))
    print(sol.isPowerOfThree(243))
