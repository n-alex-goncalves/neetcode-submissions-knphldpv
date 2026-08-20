class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        intervals = sorted(intervals, key = lambda x:x[0])
        stack = []
        for x, y in intervals:
            newStart, newEnd = x, y
            while stack and stack[-1][-1] > x:
                i, j = stack.pop()
                newStart, newEnd = max(x, i), min(y, j)
            stack.append([newStart, newEnd])
        return length - len(stack)
        