class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        output = 0
        while l < r:
            cur = min(heights[l], heights[r]) * (r - l)
            output = max(output, cur)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return output
            
        