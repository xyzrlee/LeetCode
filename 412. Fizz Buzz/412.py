class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for i in range(1, n + 1):
            div3 = i % 3 == 0
            div5 = i % 5 == 0
            if div3 and div5:
                list.append("FizzBuzz")
            elif div3:
                list.append("Fizz")
            elif div5:
                list.append("Buzz")
            else:
                list.append(str(i))
        return list


if __name__ == '__main__':
    sol = Solution()
    print(sol.fizzBuzz(15))
