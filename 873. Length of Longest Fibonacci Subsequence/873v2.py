from typing import List


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        length = len(A)
        B = set(A)
        d = {}
        for i in range(length):
            for j in range(i):
                d[(A[j], A[i])] = 2
                if A[i] - A[j] in B and (A[i] - A[j], A[j]) in d:
                    d[(A[j], A[i])] = d[(A[i] - A[j], A[j])] + 1
        m = max(d.values())
        return m if m > 2 else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
    print(sol.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
    print(sol.lenLongestFibSubseq([1, 3, 5]))
