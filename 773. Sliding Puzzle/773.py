import collections
from typing import List, Dict, Tuple, Deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        numList: List[str] = []
        for x in board:
            for y in x:
                numList.append(str(y))
        initString: str = "".join(numList)
        viewed: List[str] = []
        jump: Dict[int, List[int]] = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        def bfs(currentString: str) -> int:
            queue: Deque[Tuple[str, int]] = collections.deque()
            queue.append((currentString, 0))
            while len(queue) > 0:
                s: Tuple[str, int] = queue.popleft()
                if s[0] == "123450": return s[1]
                if s[0] in viewed: continue
                p = s[0].find("0")
                if p < 0: continue
                for i in jump[p]:
                    l = list(s[0])
                    l[p], l[i] = l[i], l[p]
                    ns: str = "".join(l)
                    if ns == "123450": return s[1] + 1
                    queue.append(("".join(l), s[1] + 1))
                viewed.append(s[0])
            return -1

        return bfs(initString)


if __name__ == '__main__':
    sol = Solution()
    print(sol.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
    print(sol.slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
    print(sol.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
    print(sol.slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
