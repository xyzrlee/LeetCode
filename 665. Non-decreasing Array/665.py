from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3: return True
        pos, changed = 0, 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if changed > 0: return False
                if i == 1 or (nums[i] >= nums[i - 2]):
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                changed += 1
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkPossibility([4, 2, 3]))
    print(sol.checkPossibility([4, 2, 1]))
    print(sol.checkPossibility([5, 7, 1, 8]))
    print(sol.checkPossibility([1, 3, 2]))
    print(sol.checkPossibility([1, 2, 4, 5, 3]))
