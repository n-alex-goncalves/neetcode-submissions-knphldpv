class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def frequencyKey(s):
            lst = [0] * 27
            for character in s:
                lst[ord(character) - 96] += 1
            return lst
        
        return frequencyKey(s) == frequencyKey(t)        