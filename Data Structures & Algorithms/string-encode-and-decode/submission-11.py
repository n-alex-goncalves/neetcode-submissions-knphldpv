class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.extend([str(len(word)), '|', word])
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        lengthLst = []
        i = 0

        while i < len(s):
            character = s[i]
            if character == '|':
                length = int("".join(lengthLst))
                output.append(s[i + 1:i + length + 1])
                lengthLst = []
                i += length + 1
            else:
                lengthLst.append(character)
                i += 1
        
        return output