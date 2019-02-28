from typing import List


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        length, m = len(A), 0
        B = set(A)
        for i in range(length):
            for j in range(i + 1, length):
                x, y, n = A[j], A[i] + A[j], 2
                while y in B: x, y, n = y, x + y, n + 1
                m = max(m, n)
        return m if m > 2 else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
    print(sol.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
