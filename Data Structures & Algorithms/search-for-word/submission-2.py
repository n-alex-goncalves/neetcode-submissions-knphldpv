class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        COL = len(board[0])
        ROW = len(board)
        self.visited = set()

        def backtrack(x, y, i):
            if (
                x < 0 or
                x >= COL or
                y < 0 or
                y >= ROW or
                (x, y) in self.visited or
                board[y][x] != word[i]
            ):
                return False
            
            if i == len(word) - 1:
                return True
            
            self.visited.add((x, y))

            output = (
                backtrack(x + 1, y, i + 1) or
                backtrack(x, y + 1, i + 1) or
                backtrack(x - 1, y, i + 1) or
                backtrack(x, y - 1, i + 1)
            )

            self.visited.remove((x, y))
            return output
        
        for x in range(COL):
            for y in range(ROW):
                if backtrack(x, y, 0):
                    return True
        
        return False
            

        