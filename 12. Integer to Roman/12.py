class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rom = ['M', 'D', 'C', 'L', 'X', 'V', 'I', '']
        val = [1000, 500, 100, 50, 10, 5, 1, 0]
        left = [False, False, True, False, True, False, True, False]
        n = num
        p = 0
        str = ''
        while n > 0:
            for q in range(6 - p):
                if left[p + q + 1]:
                    if n // val[p + q + 1] == (val[p] - val[p + q + 1]) // val[p + q + 1]:
                        str += rom[p + q + 1]
                        str += rom[p]
                        n = n - val[p] + val[p + q + 1]
                        continue
            if n >= val[p]:
                str += rom[p] * int(n / val[p])
                n = n % val[p]
                continue
            p += 1
        return str


if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(40))
