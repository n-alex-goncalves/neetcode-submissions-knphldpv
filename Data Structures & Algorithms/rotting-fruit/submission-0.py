class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = []
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    grid[r][c] = 1
        
        minTime = 0

        while queue:
            (r, c, d) = queue.pop(0) # row, column, depth

            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or grid[r][c] == 0
                or grid[r][c] == 2
            ):
                continue
            
            grid[r][c] = 2
            minTime = max(minTime, d)

            queue.extend([
                (r + 1, c, d + 1),
                (r - 1, c, d + 1),
                (r, c + 1, d + 1),
                (r, c - 1, d + 1)
            ])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        
        return minTime


        