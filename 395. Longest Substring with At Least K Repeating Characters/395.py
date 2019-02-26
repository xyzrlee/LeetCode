class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        l = []
        d = {}
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
            dd = d.copy()
            l.append(dd)
        length = len(s)
        max = 0
        for i in range(length):
            if d[s[i]] < k: continue
            if i == 0:
                di = {}
            else:
                di = l[i - 1]
            for j in range(i, length):
                if d[s[j]] < k: break;
                dj = l[j]
                x = True
                for c in dj:
                    if c in di:
                        n = dj[c] - di[c]
                    else:
                        n = dj[c]
                    if n > 0 and n < k:
                        x = False
                        break
                if x and j - i + 1 > max:
                    max = j - i + 1
        return max


if (__name__ == '__main__'):
    sol = Solution()
    n = sol.longestSubstring('bbaaacbd', 3)
    print('solution:', n)
