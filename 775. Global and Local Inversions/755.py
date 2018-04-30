class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i, n in enumerate(A):
            if (n > i and i + 1 != n) or (n < i and i - 1 != n):
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIdealPermutation([1, 0, 2]))
