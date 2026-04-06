class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
        
        visited = set()

        while queue:
            r, c, distance = queue.pop(0)

            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or (r, c) in visited
                or grid[r][c] == -1
            ):
                continue
            
            grid[r][c] = distance
            visited.add((r, c))

            queue.extend([
                (r + 1, c, distance + 1),
                (r - 1, c, distance + 1),
                (r, c + 1, distance + 1),
                (r, c - 1, distance + 1),
            ])

        

            
            

        