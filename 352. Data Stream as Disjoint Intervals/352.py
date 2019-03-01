from typing import List


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "%r" % [self.start, self.end]


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        n = len(self.intervals)
        i, j = 0, n
        while i < j:
            k = i + (j - i) // 2
            if val < self.intervals[k].start:
                j = k
            else:
                i = k + 1
        if i > 0 and self.intervals[i - 1].end >= val: return
        if 0 < i < n and self.intervals[i - 1].end + 1 == val == self.intervals[i].start - 1:
            self.intervals[i - 1].end = self.intervals[i].end
            del self.intervals[i]
        elif 0 < i and self.intervals[i - 1].end + 1 == val:
            self.intervals[i - 1].end = val
        elif i < n and self.intervals[i].start - 1 == val:
            self.intervals[i].start = val
        else:
            self.intervals.insert(i, Interval(val, val))

    def getIntervals(self) -> List[Interval]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

if __name__ == '__main__':
    s = SummaryRanges()
    x = [1, 3, 7, 2, 6]
    x = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
    for xx in x:
        s.addNum(xx)
        print(s.getIntervals())
