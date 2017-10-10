class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = (1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691)
        if n <= 10:
            return num[n]
        else:
            return num[10]

    def getCountNumbers(self):
        list = []
        sum = 0
        for i in range(11):
            n = 1
            for j in range(i):
                if j == 0:
                    n = n * 9
                else:
                    n = n * (10 - j)
            sum = sum + n
            list.append(sum)
        print(list)


if __name__ == '__main__':
    sol = Solution()
    sol.getCountNumbers()
    print(sol.countNumbersWithUniqueDigits(15))
