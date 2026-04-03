class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFreq(s: str):
            lst = [0] * 27
            for character in s:
                lst[ord(character) - 96] += 1
            return tuple(lst)
        
        dictionary = collections.defaultdict(list)
        for word in strs:
            key = getFreq(word)
            dictionary[key].append(word)
        return list(dictionary.values())