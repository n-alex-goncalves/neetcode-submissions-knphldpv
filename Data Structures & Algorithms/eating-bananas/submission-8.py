import numpy as np

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(speed, piles, h):
            return sum([np.ceil(x / speed) for x in piles]) <= h

        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if canEat(mid, piles, h):
                r = mid
            else:
                l = mid + 1
        
        return r

        