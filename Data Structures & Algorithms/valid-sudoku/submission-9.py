class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = collections.defaultdict(set)
        colDict = collections.defaultdict(set)
        boxDict = collections.defaultdict(set)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == ".":
                    continue

                if (
                    board[y][x] in rowDict[y] or
                    board[y][x] in colDict[x] or
                    board[y][x] in boxDict[(x // 3, y // 3)]
                ):
                    return False
                
                rowDict[y].add(board[y][x])
                colDict[x].add(board[y][x])
                boxDict[(x // 3, y // 3)].add(board[y][x])
        
        return True