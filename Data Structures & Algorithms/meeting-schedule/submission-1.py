"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda x:x.start)
        stack = []

        for x in intervals:
            a = x.start
            b = x.end
            if stack and stack[-1][-1] > a:
                return False
            stack.append([a, b])
        
        return True
