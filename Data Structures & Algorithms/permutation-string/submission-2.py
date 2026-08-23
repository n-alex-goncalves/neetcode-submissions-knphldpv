class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        if ord matches
        return true
        else continue
        '''

        def freqList(s: str):
            lst = [0 for _ in range(26)]
            for character in s:
                lst[ord(character) - 97] += 1
            return lst

        def freqIndex(i):
            return ord(s2[i]) - 97
        
        freqList = freqList(s1)

        l, r = 0, 0
        freqList[ord(s2[0]) - 97] -= 1
        while r < len(s2):
            if l < r and any([x < 0 for x in freqList]):
                freqList[freqIndex(l)] += 1
                l += 1
            elif any([x > 0 for x in freqList]):
                r += 1
                if r < len(s2):
                    freqList[freqIndex(r)] -= 1
            else:
                return True
        
        return False



