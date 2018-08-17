import bisect


class KthLargest:
    k = 0
    nums = []

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        nums.sort()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        bisect.insort(self.nums, val)
        return self.nums[-self.k]


if __name__ == '__main__':
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
