class Solution:
    def trap(self, height: List[int]) -> int:
        edge = 0
        left = []
        l = 0
        while l < len(height):
            left.append(edge)
            edge = max(edge, height[l])
            l += 1
        
        edge = 0
        right = []
        r = len(height) - 1
        while r > -1:
            right.append(edge)
            edge = max(edge, height[r])
            r -= 1
        right = right[::-1]

        total = 0
        i = 0
        for x, y in zip(left, right):
            total += max(0, min(x, y) - height[i])
            i += 1
        
        return total