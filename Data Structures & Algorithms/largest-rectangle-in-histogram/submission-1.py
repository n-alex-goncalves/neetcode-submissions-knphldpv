class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxLength = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][-1] > h:
                s2, h2 = stack.pop()
                maxLength = max(maxLength, h2 * (i - s2))
                start = s2
            stack.append((start, h))
        
        for i, h in stack:
            maxLength = max(maxLength, h * (len(heights) - i))
        
        return maxLength

