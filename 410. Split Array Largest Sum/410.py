import sys


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        numsLength = len(nums)
        sums = [0] * numsLength
        for i in range(numsLength):
            if i == 0:
                sums[i] = nums[i]
            else:
                sums[i] = sums[i - 1] + nums[i]
        print(sums)
        rslt = [[sys.maxsize] * (numsLength + 1)] * (m + 1)
        print(rslt)
        for i in range(m):
            for j in range(numsLength - i):
                if i == 0:
                    rslt[i][j] = sums[numsLength - 1] - sums[j]
                    print(i, j, rslt[i][j])
                else:
                    for k in range(j, numsLength - i, 1):
                        rslt[i][j] = min(max(rslt[i - 1][k], (sums[k] - sums[j])), rslt[i][j])
                        print(i, j, k, rslt[i][j])
        print(rslt)


if __name__ == '__main__':
    sol = Solution()
    print(sol.splitArray([7, 2, 5, 10, 8], 2))
