class Solution:

    def encode(self, strs: List[str]) -> str:
        lst = []
        for word in strs:
            lst.extend([
                str(len(word)),
                '|',
                word
            ])
        return ''.join(lst)
        
    def decode(self, s: str) -> List[str]:
        length = ''
        output = []
        i = 0
        while i < len(s):
            character = s[i]
            if character.isdigit():
                length += character
            else:
                output.append(s[i + 1:i + 1 + int(length)])
                i += int(length)
                length = ''
            i += 1
        return output
