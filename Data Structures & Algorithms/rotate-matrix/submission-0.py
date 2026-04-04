class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # How do I rotate a matrix?
        for c in range(len(matrix[0])):
            for i in range(len(matrix) // 2):
                matrix[i][c], matrix[len(matrix) - i - 1][c] = matrix[len(matrix) - i - 1][c], matrix[i][c]
        
        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        

