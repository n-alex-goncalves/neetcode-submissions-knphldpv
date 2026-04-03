class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getFreq(s: str):
            lst = [0] * 27
            for character in s:
                lst[ord(character) - 96] += 1
            return tuple(lst)
        
        dictionary = collections.defaultdict(list)
        for word in strs:
            frequency = getFreq(word)
            dictionary[frequency].append(word)
        
        return list(dictionary.values())