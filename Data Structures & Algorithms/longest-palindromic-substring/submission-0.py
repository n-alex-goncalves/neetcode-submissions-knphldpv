class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if s[l] == s[r]:
                    output = max(output, s[l:r+1], key=lambda x:len(x))
                    l -= 1
                    r += 1
                    continue
                r = len(s)
            
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    output = max(output, s[l:r+1], key=lambda x:len(x))
                    l -= 1
                    r += 1
                    continue
                r = len(s)
        
        return output
        