import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        result = 0
        diff = sys.maxsize
        for i in range(l - 2):
            j, k = i + 1, l - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                d = abs(sum - target)
                if d < diff:
                    diff = d
                    result = sum
                if sum < target:
                    j += 1
                if sum > target:
                    k -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))
