class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        second and below total - k > 0
        get first minus total
        running max? or just find? 26? not large
        find()
        '''
        lst = [0] * 26
        maxLength = 1

        def index(i, s=s):
            return ord(s[i].lower()) - 97
        
        lst[index(0)] += 1
        l, r = 0, 0
        while r < len(s):
            print(lst[:2], maxLength)
            if sum(lst) - max(lst) - k > 0:
                lst[index(l)] -= 1
                l += 1
            else:
                maxLength = max(maxLength, r - l + 1)
                r += 1
                if r < len(s):
                    lst[index(r)] += 1
        return maxLength


        