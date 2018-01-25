class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            result = str(nums[0]) + '/(' + str(nums[1])
            for i in nums[2:]:
                result += '/' + str(i)
            result += ')'
            return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.optimalDivision([1, 2, 3, 4]))
