class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i, character in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != character:
                    return prefix
            prefix += character
        return prefix
            

        