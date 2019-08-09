from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        result, l, t = 0, 0, 0
        for i in range(len(A)):
            if L <= A[i] <= R:
                t = i - l + 1
                result += t
            elif A[i] < L:
                result += t
            else:
                t = 0
                l = i + 1
            i += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
