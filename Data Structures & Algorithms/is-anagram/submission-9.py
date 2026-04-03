class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def getFreqKey(s: str):
            lst = [0] * 27
            for character in s:
                lst[ord(character) - 96] += 1
            return lst

        return getFreqKey(s) == getFreqKey(t)
        