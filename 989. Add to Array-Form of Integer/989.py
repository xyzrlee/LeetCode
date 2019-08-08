import copy
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        k = K
        result = copy.deepcopy(A)
        for p in range(len(result) - 1, -1, -1):
            if (k <= 0):
                break
            result[p] += k
            k, result[p] = divmod(result[p], 10)
        result = list(map(int, str(k))) + result if k > 0 else result
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.addToArrayForm([1], 1))
    print(sol.addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 100))
