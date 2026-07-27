class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        tabulation
        memoization
        '''
        def dp(i, memo={}):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            lst = [(j, s[i:j]) for j in range(i + 1, len(s) + 1)]
            memo[i] = any([dp(j) for j, x in lst if x in wordDict])
            return memo[i]
        
        return dp(0)
        