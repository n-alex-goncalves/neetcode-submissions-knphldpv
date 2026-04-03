class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        iterate
        replace 1s with '.'
        count += 1
        then iterate
        '''
        def replace(col, row):
            if (
                col < 0 
                or col >= len(grid)
                or row < 0
                or row >= len(grid[0])
                or grid[col][row] == '.'
                or grid[col][row] == '0'
            ):
                return
            
            grid[col][row] = '.'
            replace(col + 1, row)
            replace(col - 1, row)
            replace(col, row + 1)
            replace(col, row - 1)

        count = 0
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if grid[col][row] == '1':
                    count += 1
                    replace(col, row)
        return count

        