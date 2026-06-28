class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFrequencyTuple(s: str):
            lst = [0] * 26
            for c in s:
                lst[ord(c) - 97] += 1
            return tuple(lst)
        
        dictionary = collections.defaultdict(list)
        for word in strs:
            key = getFrequencyTuple(word)
            dictionary[key].append(word)
        
        return list(dictionary.values())
