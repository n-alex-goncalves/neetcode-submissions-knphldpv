class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0 
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    output += 1
                    l -= 1
                    r += 1
                else:
                    r = len(s)
            
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    output += 1
                    l -= 1
                    r += 1
                else:
                    r = len(s)
        
        return output
        