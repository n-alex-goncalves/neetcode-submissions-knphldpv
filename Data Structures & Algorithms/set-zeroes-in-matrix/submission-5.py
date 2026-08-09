class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setFirstRowZero = any([i == 0 for i in matrix[0]])
        
        col = [matrix[j][0] for j in range(len(matrix))]
        setFirstColZero = any([i == 0 for i in col])
    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
                elif matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if setFirstRowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if setFirstColZero:
            for j in range(len(matrix)):
                matrix[j][0] = 0

        
        