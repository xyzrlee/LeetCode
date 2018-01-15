class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        result = 0
        map = {}
        for a in A:
            for b in B:
                if a + b in map:
                    map[a + b] += 1
                else:
                    map[a + b] = 1
        for c in C:
            for d in D:
                if -c - d in map:
                    result += map[-c - d]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSumCount([-1, -1], [-1, 1], [-1, 1], [1, -1]))
