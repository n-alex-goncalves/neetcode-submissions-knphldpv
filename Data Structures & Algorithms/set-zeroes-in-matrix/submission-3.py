class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:        
        firstRowZero = any(matrix[r][0] == 0 for r in range(len(matrix)))
        firstColZero = any(matrix[0][c] == 0 for c in range(len(matrix[0])))

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Setting zero across matrix

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        for r in range(len(matrix)):
            if firstRowZero:
                matrix[r][0] = 0
        
        for c in range(len(matrix[0])):
            if firstColZero:
                matrix[0][c] = 0
