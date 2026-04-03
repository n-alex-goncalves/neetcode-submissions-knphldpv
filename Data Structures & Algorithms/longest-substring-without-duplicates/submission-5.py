class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = collections.defaultdict(int)
        l = 0
        r = 0
        maxLength = 0

        if not s:
            return 0

        dictionary[s[r]] += 1
        while r < len(s):
            if any([x > 1 for x in dictionary.values()]):
                dictionary[s[l]] -= 1
                l += 1
            else:
                maxLength = max(maxLength, r - l + 1)
                r += 1
                if r < len(s):
                    dictionary[s[r]] += 1
        
        return maxLength