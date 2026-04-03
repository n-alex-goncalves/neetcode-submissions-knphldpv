class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(col, row, word):
            if (
                col < 0 or
                col >= len(board) or
                row < 0 or 
                row >= len(board[0]) or
                board[col][row] == '.' or
                board[col][row] != word[0]
            ):
                return False
            
            if len(word) == 1:
                return True

            temp = board[col][row]
            board[col][row] = '.'
            output = (
                search(col + 1, row, word[1:]) or
                search(col - 1, row, word[1:]) or
                search(col, row + 1, word[1:]) or
                search(col, row - 1, word[1:])
            )
            board[col][row] = temp
            return output


        for col in range(len(board)):
            for row in range(len(board[0])):
                if search(col, row, word):
                    return True
        
        return False
        