class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        
        for r in range(len(text2) - 1, -1, -1):
            for c in range(len(text1) - 1, -1, -1):
                if text2[r] == text1[c]:
                    table[r][c] += 1 + table[r + 1][c + 1]
                else:
                    table[r][c] = max(table[r + 1][c], table[r][c + 1])

        return table[0][0]
                
