import re


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        m = re.match("[ ]*([+-]?)([0-9]*)", str, re.M | re.I)
        if m == None:
            return 0
        symbol = m.group(1)
        isNegative = symbol == "-"
        digits = m.group(2)
        digits = digits.lstrip("0")
        if digits == "":
            return 0
        isOverflow = False
        if 10 < len(digits):
            isOverflow = True
        else:
            if 10 == len(digits):
                if isNegative and digits > "2147483648":
                    isOverflow = True
                if not isNegative and digits > "2147483647":
                    isOverflow = True
        if isOverflow:
            if isNegative:
                return -2147483648
            else:
                return 2147483647
        return int(symbol + digits)


if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi("  0000000000012345678"))
