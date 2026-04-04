class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(s, memo={}):
            if s in memo:
                return memo[s]
            if not s:
                return True

            for word in wordDict:
                length = len(word)
                if s[:length] in wordDict and dp(s[length:], memo):
                    memo[s] = True
                    return memo[s]

            memo[s] = False
            return memo[s]
        
        return dp(s)
            

        