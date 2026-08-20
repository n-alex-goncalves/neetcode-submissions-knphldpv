class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        stack = []
        for x, y in intervals:
            newStart, newEnd = x, y
            if stack and stack[-1][-1] >= x:
                i, j = stack.pop()
                newStart, newEnd = min(x, i), max(y, j)
            stack.append([newStart, newEnd])
        return stack
        