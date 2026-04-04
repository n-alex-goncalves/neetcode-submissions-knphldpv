class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        output = []
        for start, end in intervals:
            if output and output[-1][-1] >= start:
                output[-1][-1] = max(output[-1][-1], end)
            else:
                output.append([start, end])
        return output        