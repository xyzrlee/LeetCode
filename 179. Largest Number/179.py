class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        strs = [str(x) for x in nums]
        strs.sort(key=cmp_to_key(lambda x, y: 1 if y + x > x + y else -1))
        return ''.join(strs).lstrip('0') or '0'


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([3, 30, 34, 5, 9]))
