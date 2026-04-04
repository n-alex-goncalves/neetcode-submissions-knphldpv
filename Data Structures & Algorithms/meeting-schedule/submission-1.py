"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = [[x.start, x.end] for x in intervals]
        intervals = sorted(intervals, key=lambda x:x[0])
        prev = None
        for start, end in intervals:
            if prev and prev[-1] > start:
                return False
            else:
                prev = [start, end]
        return True
