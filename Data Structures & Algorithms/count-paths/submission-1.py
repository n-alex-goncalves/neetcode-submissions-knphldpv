class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        tabulationtable
$0
        memoization

        bottom-up tabulation
        top-down memoization


        '''
        table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        table[m ][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                table[i][j] = table[i + 1][j] + table[i][j + 1]
        
        for row in table:
            print(row)

        return table[0][0]
