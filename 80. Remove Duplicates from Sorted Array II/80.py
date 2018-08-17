class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        x, n = nums[0], 0
        while i < len(nums):
            nc = nums[i]
            if x == nc:
                n += 1
                if n > 2:
                    nums.remove(nc)
                    continue
            else:
                x = nc
                n = 1
            i += 1
        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(sol.removeDuplicates(nums))
    print(nums)
