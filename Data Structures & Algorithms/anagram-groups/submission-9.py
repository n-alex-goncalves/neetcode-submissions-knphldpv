class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFreqKey(s):
            lst = [0] * 26
            for character in s:
                lst[ord(character) - 97] += 1
            return tuple(lst)
        
        dictionary = collections.defaultdict(list)
        for word in strs:
            dictionary[getFreqKey(word)].append(word)
        return list(dictionary.values())
