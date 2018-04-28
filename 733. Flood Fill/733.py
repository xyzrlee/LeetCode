class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        lr, lc = len(image), len(image[0])
        oldColor = image[sr][sc]
        if newColor == oldColor: return image

        def dfs(r, c):
            print(r, c, image[r][c])
            if image[r][c] == oldColor:
                image[r][c] = newColor
                if r > 0: dfs(r - 1, c)
                if r + 1 < lr: dfs(r + 1, c)
                if c > 0: dfs(r, c - 1)
                if c + 1 < lc: dfs(r, c + 1)

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    sol = Solution()
    # print(sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
    print(sol.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
