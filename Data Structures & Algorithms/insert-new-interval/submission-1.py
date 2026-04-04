class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x:x[0])
        output = []
        for start, end in intervals:
            if output and output[-1][-1] >= start:
                output[-1][-1] = max(end, output[-1][-1])
            else:
                output.append([start, end])
        return output

        