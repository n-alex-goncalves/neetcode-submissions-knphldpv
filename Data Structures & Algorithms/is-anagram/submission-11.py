class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def getFrequencyList(s: str):
            lst = [0] * 26
            for character in s:
                lst[ord(character) - 97] += 1
            return lst
        
        return getFrequencyList(s) == getFrequencyList(t)