class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def spread(x, y):
            if (
                y < 0 or
                y >= len(grid) or
                x < 0 or 
                x >= len(grid[0]) or
                grid[y][x] == "2" or
                grid[y][x] == "0"
            ):
                return
            
            grid[y][x] = "2"

            spread(x + 1, y)
            spread(x - 1, y)
            spread(x, y + 1)
            spread(x, y - 1)

            return
        
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                  output += 1
                  spread(j, i)
                
        
        return output
        