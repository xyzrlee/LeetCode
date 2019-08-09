import collections
import copy
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = collections.deque()
        d = copy.deepcopy(deck)
        d.sort(reverse=True)
        for x in d:
            q.appendleft(q.pop()) if len(q) > 0 else None
            q.appendleft(x)
        return list(q)


if __name__ == '__main__':
    sol = Solution()
    print(sol.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
