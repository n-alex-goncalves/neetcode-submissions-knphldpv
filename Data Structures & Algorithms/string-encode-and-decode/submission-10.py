class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for word in strs:
            code += str(len(word)) + '|' + word
        return code

    def decode(self, s: str) -> List[str]:
        lst = []
        length = len(s)
        i = 0
        j = 0

        while i < length:
            while s[j].isdigit():
                j += 1

            lengthOfWord = int(s[i:j])
            lst.append(s[j+1:j+1+lengthOfWord])

            i = j + 1 + lengthOfWord
            j = i
        
        return lst