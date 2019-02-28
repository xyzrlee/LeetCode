class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numx = nums.copy()
        nums.sort()
        i, j = 0, len(nums) - 1
        while i <= j and nums[i] == numx[i]:
            i += 1
        while i <= j and nums[j] == numx[j]:
            j -= 1
        k = j - i + 1
        return k


if __name__ == '__main__':
    sol = Solution()
    sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
    sol.findUnsortedSubarray([1, 2, 3])
    sol.findUnsortedSubarray([1])
