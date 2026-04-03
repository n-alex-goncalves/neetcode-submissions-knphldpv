import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findHour(piles, k):
            return sum([math.ceil(x / k) for x in piles])

        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            cur = findHour(piles, mid)
            if cur > h:
                l = mid + 1
            else:
                r = mid
        return l