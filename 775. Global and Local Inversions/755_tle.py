class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        nLocal = nGlobal = 0
        for i in range(len(A)):
            if i + 1 < len(A) and A[i] > A[i + 1]:
                nLocal += 1
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    nGlobal += 1
        return nLocal == nGlobal


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIdealPermutation([1, 0, 2]))
