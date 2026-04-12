class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        borders = [0, len(matrix[0]) - 1, 0, len(matrix) - 1] 
        # left, right, up, down
        self.output = []

        def spiral(r, c, direction):
            if (
                r < 0 or
                r > len(matrix) or
                c < 0 or
                c > len(matrix[0]) or
                len(self.output) == len(matrix) * len(matrix[0])
            ):
                return
            
            self.output.append(matrix[r][c])

            if direction == 'U':
                if r == borders[2]: # UP
                    borders[0] += 1 # LEFT
                    spiral(r, c + 1, 'R')
                else:
                    spiral(r - 1, c, 'U')
            
            if direction == 'D':
                if r == borders[3]: # DOWN
                    borders[1] -= 1 # RIGHT
                    spiral(r, c - 1,  'L')
                else:
                    spiral(r + 1, c, 'D')
            
            if direction == 'L':
                if c == borders[0]: # LEFT
                    borders[3] -= 1 # DOWN
                    spiral(r - 1, c, 'U')
                else:
                    spiral(r, c - 1, 'L')
            
            if direction == 'R':
                if c == borders[1]:
                    borders[2] += 1
                    spiral(r + 1, c, 'D')
                else:
                    spiral(r, c + 1, 'R')
            
            return
        
        spiral(0, 0, 'R')
        return self.output

        