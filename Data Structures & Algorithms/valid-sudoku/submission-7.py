class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colDict = collections.defaultdict(list)
        boxDict = collections.defaultdict(list)
        rowDict = collections.defaultdict(list)

        for row in range(0, 9):
            for col in range(0, 9):
                value = board[row][col]

                if value == '.':
                    continue
                
                if (
                    value in colDict[col] or 
                    value in boxDict[(row // 3, col // 3)] or 
                    value in rowDict[row]
                ):
                    return False
                
                colDict[col].append(value)
                rowDict[row].append(value)
                boxDict[(row // 3, col // 3)].append(value)

        return True
        