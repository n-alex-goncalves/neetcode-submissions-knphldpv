class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        a   b   c
    a   T
    b       T   
    c           T
        '''
        table = [[False for _ in range(len(s))] for _ in range(len(s))]
        self.output = len(s)

        for i in range(0, len(s)):
            for j in range(0, i + 1):
                table[i][j] = True

        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if (
                    s[i] == s[j] and
                    table[i + 1][j - 1]
                ):
                    table[i][j] = True
                    self.output += 1
        
        return self.output


        