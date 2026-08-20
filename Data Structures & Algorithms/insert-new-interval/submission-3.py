class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x:x[0])

        stack = []
        for x, y in intervals:
            newStart, newEnd = x, y
            while stack and stack[-1][-1] >= x:
                i, j = stack.pop()
                newStart, newEnd = min(x, i), max(y, j)
            stack.append([newStart, newEnd])
        
        return stack
            
