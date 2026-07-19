class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        tabulation
        base case
        1 character
        2 characters
        look up function for converting numbers into alphabet
        123
        '''
        table = [0] * len(s)

        if 0 < int(s[0]) < 10:
            table[0] += 1

        if len(s) == 1:
            return table[0]

        if 0 < int(s[1]) < 10:
            table[1] += table[0]

        if 0 < int(s[:2]) < 27 and s[0] != '0':
            table[1] += 1

        for i in range(2, len(s)):
            if 0 < int(s[i-1:i+1]) < 27 and s[i - 1] != '0':
                table[i] += table[i - 2]
            if 0 < int(s[i]) < 10 and s[i] != '0':
                table[i] += table[i - 1]
        
        print(table)
        return table[-1]




        