class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        a   b   a   b   d   a
    a   T   F  T   F   F  F
    b       T   F  T   F   F
    a           T   F  F   F
    b               T  F   F
    d                   T   F
    a                       T
        '''
        self.maxLength = 1
        self.output = s[0]

        table = [[False for _ in range(len(s))] for _ in range(len(s))]
    
        for i in range(0, len(s)):
            for j in range(0, i + 1):
                table[i][j] = True
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if (
                    s[i] == s[j] and
                    table[i + 1][j - 1] == True
                ):
                    table[i][j] = True
                    if j - i + 1 > self.maxLength:
                        self.maxLength = j - i + 1
                        self.output = s[i:j + 1]


        return self.output
