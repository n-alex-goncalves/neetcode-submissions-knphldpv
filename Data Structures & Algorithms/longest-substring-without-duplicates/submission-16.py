class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = [0] * 60
        self.s = s
        self.maxLength = 0

        if not s:
            return 0

        def index(i):
            if self.s[i] == " ":
                return 59
            return ord(self.s[i]) - 65

        l, r = 0, 0
        lst[index(0)] += 1
        
        while r < len(s):
            if any([x > 1 for x in lst]):
                lst[index(l)] -= 1
                l += 1
            else:
                self.maxLength = max(r - l + 1, self.maxLength)
                r += 1
                if r < len(s):
                    lst[index(r)] += 1
        
        return self.maxLength