class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = collections.defaultdict(list)
        colDict = collections.defaultdict(list)
        boxDict = collections.defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if (
                    board[i][j] in rowDict[i] or
                    board[i][j] in colDict[j] or
                    board[i][j] in boxDict[(i // 3, j // 3)]
                ):
                    return False
                
                rowDict[i].append(board[i][j])
                colDict[j].append(board[i][j])
                boxDict[(i // 3, j // 3)].append(board[i][j])
        
        return True