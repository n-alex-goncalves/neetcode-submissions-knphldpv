class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dp

        either right or down
        '''

        def dp(m, n, memo={}):
            if (m, n) in memo:
                return memo[(m, n)]
            
            if m < 0 or n < 0:
                return 0

            if m == 0 and n == 0:
                return 1
            
            memo[(m, n)] = dp(m - 1, n) + dp(m, n - 1)
            return memo[(m, n)]
        
        return dp(m - 1, n - 1)
        