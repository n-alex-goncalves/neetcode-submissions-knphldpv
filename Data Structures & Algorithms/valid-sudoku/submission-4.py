class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxDict = collections.defaultdict(list)
        colDict = collections.defaultdict(list)
        rowDict = collections.defaultdict(list)

        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == '.':
                    continue
                
                if (
                    board[row][col] in boxDict[(row // 3, col // 3)] or
                    board[row][col] in rowDict[row] or
                    board[row][col] in colDict[col]
                ):
                    return False
                
                boxDict[(row // 3, col // 3)].append(board[row][col])
                rowDict[row].append(board[row][col])
                colDict[col].append(board[row][col])

        return True
                
        