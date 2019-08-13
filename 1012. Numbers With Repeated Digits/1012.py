class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        list_n = list(map(int, str(N + 1)))
        res = 0
        len_n = len(list_n)

        for i in range(1, len_n):
            res += 9 * self.get_cnt(9, i - 1)

        s = set()
        for i, x in enumerate(list_n):
            for y in range(0 if i else 1, x):
                if y in s: continue
                res += self.get_cnt(9 - i, len_n - i - 1)
            if x in s: break
            s.add(x)

        return N - res

    def get_cnt(self, m: int, n: int) -> int:
        if 0 == n: return 1
        return self.get_cnt(m, n - 1) * (m - n + 1)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.numDupDigitsAtMostN(20))
    print(sol.numDupDigitsAtMostN(100))
    print(sol.numDupDigitsAtMostN(6718458))
