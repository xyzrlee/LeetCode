from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        x = set()
        y = []
        for i in range(len(s) - 9):
            z = s[i:i + 10]
            y.append(z) if z in x else x.add(z)
        return list(set(y))


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRepeatedDnaSequences('AAAAAAAAAAA'))
    print(sol.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
