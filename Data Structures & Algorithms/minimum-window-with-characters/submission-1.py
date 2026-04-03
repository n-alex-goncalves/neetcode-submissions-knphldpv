class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        l, r = 0, 0
        condition r = if any(frequency in t > frequency in s (only applies to characters in t))
        condition l = ^ when the above condition is not true
         shortest substring

        minLength = np.inf
        minSubstring = ""
        '''
        l, r = 0, 0

        def getFreq(s: str):
            lst = [0] * 58
            for c in s:
                lst[ord(c) - 65] += 1
            return lst
        
        tFreq = getFreq(t)
        sFreq = [0] * 58

        sFreq[ord(s[0]) - 65] += 1

        minLength = float("inf")
        minSubstring = ""

        while r < len(s):
            # print(l, r, s[l:r+1])
            # print(sFreq)
            # print(tFreq)
            if any(x > y for x, y in zip(tFreq, sFreq)):
                r += 1
                if r < len(s):
                    sFreq[ord(s[r]) - 65] += 1
            else:
                if minLength > r - l + 1:
                    minLength = r - l + 1
                    minSubstring = s[l:r+1]
                sFreq[ord(s[l]) - 65] -= 1
                l += 1
        
        while l < len(s) and not any(x > y for x, y in zip(tFreq, sFreq)):
            if minLength > r - l + 1:
                minLength = r - l + 1
                minSubstring = s[l:r+1]
            sFreq[ord(s[l]) - 65] -= 1
            l += 1
        
        return minSubstring

                
