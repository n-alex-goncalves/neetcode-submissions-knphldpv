class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxList = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        
        def checkBox():
            for box1 in boxList:
                for box2 in boxList:
                    if not checkValid([board[x][y] for x in box1 for y in box2]):
                        return False
            return True
        
        def checkRow():
            for i in range(9):
                if not checkValid(board[i]):
                    return False
            return True

        def checkCol():
            for i in range(9):
                if not checkValid([board[y][i] for y in range(9)]):
                    return False
            return True

        def checkValid(lst):
            lst = [x for x in lst if x != "."]
            return len(set(lst)) == len(lst)
        
        return checkRow() and checkCol() and checkBox()

