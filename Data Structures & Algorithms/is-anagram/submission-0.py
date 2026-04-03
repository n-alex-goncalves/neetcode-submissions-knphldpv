import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)

        for character in t:
            if s_dict.get(character) != t_dict.get(character):
                return False
        
        return True
