class Solution:
    def trap(self, height: List[int]) -> int:
        l = []
        maxHeight = 0
        for h in height:
            maxHeight = max(maxHeight, h)
            l.append(maxHeight)
        
        r = []
        maxHeight = 0
        for h in height[::-1]:
            maxHeight = max(maxHeight, h)
            r.append(maxHeight)
        r = r[::-1]

        output = 0
        for i, h in enumerate(height):
            output += min(l[i], r[i]) - h
        return output

        