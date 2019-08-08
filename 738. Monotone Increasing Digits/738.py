import math


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if (N < 10):
            return N
        result = 0
        l = int(math.log10(N))
        for i in range(l, -1, -1):
            digit = math.floor(N / math.pow(10, i)) % 10
            left = result % 10
            if left <= digit:
                result = result * 10 + digit
            else:
                x = self.monotoneIncreasingDigits(result - 1)
                p = int(pow(10, i + 1))
                y = p - 1
                result = x * p + y
                break
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.monotoneIncreasingDigits(10))
    print(sol.monotoneIncreasingDigits(1234))
    print(sol.monotoneIncreasingDigits(332))
    print(sol.monotoneIncreasingDigits(20))
    print(sol.monotoneIncreasingDigits(100))
