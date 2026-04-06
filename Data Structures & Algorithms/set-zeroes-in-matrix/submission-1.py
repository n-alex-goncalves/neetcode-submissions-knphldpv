class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def changeRow(r, val):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    matrix[r][c] = val

        def changeCol(c, val):
            for r in range(len(matrix)):
                if matrix[r][c] != 0:
                    matrix[r][c] = val


        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    changeRow(r, '.')
                    changeCol(c, '.')
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '.':
                    matrix[r][c] = 0

        
        