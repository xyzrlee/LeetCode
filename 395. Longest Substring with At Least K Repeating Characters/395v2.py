import collections


class Solution:
    def longestSubstring(self, s, k):
        """
        Idea: Use Two-pointer start and end
        Time: O(n)
        """

        # define helper function which will be recursively used
        def helper(start, end):
            count = collections.defaultdict(int)
            for i in range(start, end):
                count[s[i]] += 1
            max_len = 0
            # reset the i as the start index
            i = start
            while i < end:
                # move the left pointer when all count < k
                while i < end and count[s[i]] < k:
                    i += 1
                # set the right pointer j, starting from i
                j = i
                # move the right pointer, all count >= k
                while j < end and count[s[j]] >= k:
                    j += 1
                if i == start and j == end:
                    return end - start
                max_len = max(max_len, helper(i, j))
                # reset i to j
                i = j
            return max_len

        start, end = 0, len(s)
        return helper(start, end)
