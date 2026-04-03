class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxDict = collections.defaultdict(list)
        colDict = collections.defaultdict(list)
        rowDict = collections.defaultdict(list)

        ROW = len(board)
        COL = len(board[0])

        for i in range(ROW):
            for j in range(COL):
                cur = board[i][j]
                if cur == '.':
                    continue

                if (
                    cur in boxDict[(i // 3, j // 3)] or
                    cur in rowDict[i] or
                    cur in colDict[j]
                ):
                    return False
                
                boxDict[(i // 3, j // 3)].append(cur)
                rowDict[i].append(cur)
                colDict[j].append(cur)

        return True