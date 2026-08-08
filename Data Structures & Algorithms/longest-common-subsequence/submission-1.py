class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        tabulation - bottom-up
        memoization - top-down

        c   r   a   b   t
    c   3   2   2   1   1              
    a   2   2   2   1   1
    t   1   1   1   1   1

    if c = c:
        table[-1][-1] + 1
    else:
        max(table left and right)
        '''
        table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    table[i][j] = table[i + 1][j + 1] + 1
                else:
                    table[i][j] = max(table[i + 1][j], table[i][j + 1])
        
        return table[0][0]

        
        