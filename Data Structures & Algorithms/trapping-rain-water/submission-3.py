class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        l = 0 
        for h in height:
            left.append(l)
            l = max(l, h)
        
        right = []
        r = 0
        for h in height[::-1]:
            right.append(r)
            r = max(r, h)
        right = right[::-1]
        
        total = 0
        for l, r, h in zip(left, right, height):
            total += max(0, min(l, r) - h)
        return total
        