class Solution:
    def numDecodings(self, s: str) -> int:
        table = [0] * len(s)
        def dp(string, memo={}):
            if string in memo:
                return memo[string]
            
            if not string:
                return 1

            if string[0] == '0':
                memo[string] = 0
                return memo[string]
            
            if (
                int(string[0]) > 2 or
                int(string[:2]) > 26 or
                len(string) == 1
            ):
                memo[string] = dp(string[1:])
            else:
                memo[string] = dp(string[1:]) + dp(string[2:])

            return memo[string]
        
        return dp(s)
            