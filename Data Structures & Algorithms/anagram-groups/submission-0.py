class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getAngramCode(s):
            s_dict = collections.Counter(s)
            s_list = sorted(list(s_dict.items()), key = lambda x : x[0])
            return tuple(s_list)

        dictionary = collections.defaultdict(list)
        for s in strs:
            dictionary[getAngramCode(s)].append(s)
            
        return list(dictionary.values())