class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def getFreq(s: str):
            lst = [0] * 27
            for character in s:
                lst[ord(character) - 96] += 1
            return lst
        
        return getFreq(s) == getFreq(t)