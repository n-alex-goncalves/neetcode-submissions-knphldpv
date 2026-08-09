class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        transport then flip
        '''
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                if i == j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]
        
            