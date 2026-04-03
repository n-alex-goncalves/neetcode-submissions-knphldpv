class Solution:

    def encode(self, strs: List[str]) -> str:
        lst = []
        for word in strs:
            lst.append(str(len(word)))
            lst.append('|')
            lst.append(word)
        return ''.join(lst)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '|':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j + length + 1
        
        return res