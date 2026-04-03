import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sDictionary = collections.Counter(s)
        tDictionary = collections.Counter(t)

        for character in s:
            if sDictionary[character] != tDictionary.get(character):
                return False
        
        return True