import collections
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if 0 == len(dislikes): return True
        ddict = collections.defaultdict(list)
        for i in dislikes:
            ddict[i[0]].append(i[1])
            ddict[i[1]].append(i[0])
        map = collections.defaultdict(lambda: 0)
        for i in range(1, N + 1, 1):
            if not map[i] == 0: continue
            map[i] = 1
            q = [i]
            while q:
                n = q.pop()
                y = map[n]
                for x in ddict[n]:
                    if map[x] == 0:
                        map[x] = 0 - y
                        q.append(x)
                    elif map[x] == 0 - y:
                        continue
                    else:
                        return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
    print(sol.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]]))
    print(sol.possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
