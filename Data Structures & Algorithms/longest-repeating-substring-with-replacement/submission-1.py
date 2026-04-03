class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        everything after the first most > k = condition
        counter

        '''
        l, r = 0, 0
        longestLength = 0
        dictionary = collections.defaultdict(int)
        dictionary[s[l]] += 1

        while r < len(s):
            if  r - l + 1 - max(dictionary.values()) > k:
                dictionary[s[l]] -= 1
                l += 1
            else:
                longestLength = max(longestLength, r - l + 1)
                r += 1
                if r < len(s):
                    dictionary[s[r]] += 1
        
        return longestLength