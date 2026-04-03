class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        l, r = 0, 0
        condition r = all characters in s1 must exist in s2[l:r]
        condition l = characters that aren't in s1 (r + l - 1 > len(s1))

        adjust the substring 
        '''

        l, r = 0, 0

        def getFreq(s: str):
            lst = [0] * 27
            for character in s:
                lst[ord(character) - 97] += 1
            return lst
        
        s1Frequency = getFreq(s1)
        s2Frequency = [0] * 27

        s2Frequency[ord(s2[0]) - 97] += 1

        while r < len(s2):
            # print(l, r, s2[l:r+1])
            # print(s1Frequency)
            # print(s2Frequency)
            if any([x > y for x, y in zip(s1Frequency, s2Frequency)]):
                r += 1
                if r < len(s2):
                    s2Frequency[ord(s2[r]) - 97] += 1
            else:
                if s1Frequency == s2Frequency: # could be faster?
                    return True
                s2Frequency[ord(s2[l]) - 97] -= 1
                l += 1
        
        while l < len(s2):
            if s1Frequency == s2Frequency: # could be faster?
                return True
            s2Frequency[ord(s2[l]) - 97] -= 1
            l += 1
        
        return False






        