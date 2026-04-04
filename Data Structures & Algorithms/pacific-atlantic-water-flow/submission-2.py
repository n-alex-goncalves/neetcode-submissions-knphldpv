class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def spread(r, c, prev, ocean):
            if (
                r < 0 or
                r >= len(heights) or
                c < 0 or
                c >= len(heights[0]) or
                (r, c) in ocean or
                heights[r][c] < prev
            ):
                return

            ocean.add((r, c))

            spread(r + 1, c, heights[r][c], ocean)
            spread(r - 1, c, heights[r][c], ocean)
            spread(r, c + 1, heights[r][c], ocean)
            spread(r, c - 1, heights[r][c], ocean)

        for r in range(len(heights)):
            spread(r, 0, float('-inf'), pacific)
            spread(r, len(heights[0]) - 1, float('-inf'), atlantic)
        
        for c in range(len(heights[0])):
            spread(0, c, float('-inf'), pacific)
            spread(len(heights) - 1, c, float('-inf'), atlantic)
        
        lst = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific and (r, c) in atlantic:
                    lst.append((r, c))
        return lst