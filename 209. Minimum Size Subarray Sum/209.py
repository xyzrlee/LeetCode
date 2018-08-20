class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        sum = 0
        l = len(nums) + 1
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= s:
                l = min(l, j - i + 1)
                sum -= nums[i]
                i += 1
        if l > len(nums): return 0
        return l


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
