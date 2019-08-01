from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(sol.findKthLargest([-1, 2, 0], 2))
