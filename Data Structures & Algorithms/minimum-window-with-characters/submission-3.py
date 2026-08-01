class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        tFreq = []
        sFreq = []


        lst = [0] * 65
        for character in s:
            lst[ord(character) - 65] += 1
        
        '''
        output = [0, float('inf')]
        setT = set(t)
        l, r = 0, 0
        
        def createFrequencyList(s: string):
            lst = [0] * 65
            for character in s:
                lst[ord(character) - 65] += 1
            return lst

        tFreq = createFrequencyList(t)
        tFreq[ord(s[0]) - 65] -= 1

        while r < len(s):
            if all([x <= 0 for x in tFreq]) and l <= r:
                if r - l < output[1] - output[0]:
                    output = [l, r]
                if s[l] in setT:
                    tFreq[ord(s[l]) - 65] += 1
                l += 1
            else:
                r += 1
                if r < len(s) and s[r] in setT:
                    tFreq[ord(s[r]) - 65] -= 1
        
        if output[1] == float('inf'):
            return ""
        
        print(output)
        return s[output[0]:output[1] + 1]
