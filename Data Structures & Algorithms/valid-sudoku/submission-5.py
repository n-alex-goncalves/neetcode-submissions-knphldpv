class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxDict = collections.defaultdict(set)
        rowDict = collections.defaultdict(set)
        colDict = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[col][row]
                if val == '.':
                    continue
                
                if (
                    val in boxDict[(row // 3, col // 3)] or
                    val in rowDict[row] or
                    val in colDict[col]
                ):
                    return False
                
                boxDict[(row // 3, col // 3)].add(val)
                rowDict[row].add(val)
                colDict[col].add(val)
        
        return True
        