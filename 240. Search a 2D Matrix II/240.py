class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        lx = len(matrix)
        if lx == 0: return False
        ly = len(matrix[0])
        if ly == 0: return False
        x = lx - 1
        y = 0
        while x >= 0 and y < ly:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
