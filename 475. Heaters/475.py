import bisect
import sys
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        result = -1
        for pos in houses:
            k = bisect.bisect(heaters, pos)
            l = pos - heaters[k - 1] if k > 0 else sys.maxsize
            r = heaters[k] - pos if (k < len(heaters)) else sys.maxsize
            result = max(result, min(l, r))
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRadius([1, 2, 3, 4], [1, 4]))
