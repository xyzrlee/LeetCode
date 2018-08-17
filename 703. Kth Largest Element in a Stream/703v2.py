import heapq


class KthLargest:
    k = 0
    nums = []
    size = 0

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.size = len(nums)
        heapq.heapify(self.nums)
        while len(nums) > self.k:
            heapq.heappop(self.nums)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.nums, val)
            self.size += 1
        else:
            if self.nums[0] < val:
                heapq.heapreplace(self.nums, val)
        return self.nums[0]


if __name__ == '__main__':
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
