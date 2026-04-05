class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        self.output = 0

        backtrack()
        return size 
        compare with self.output
        '''
        output = 0

        def backtrack(r, c):
            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or grid[r][c] == 0
                or grid[r][c] == '.'
            ):
                return 0
            
            grid[r][c] = '.'

            area = (
                1 +
                backtrack(r + 1, c) +
                backtrack(r - 1, c) +
                backtrack(r, c + 1) +
                backtrack(r, c - 1)
            )

            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    output = max(output, backtrack(r, c))
        
        return output
            

        