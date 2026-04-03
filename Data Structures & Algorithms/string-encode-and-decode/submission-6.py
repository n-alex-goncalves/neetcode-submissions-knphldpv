class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for string in strs:
            length = len(string)
            code += str(length) + "#" + string
        return code

    def decode(self, s: str) -> List[str]:
        output = []
        length = len(s)
        l, r = 0, 0
        while r < length:
            if s[r] == '#':
                lengthOfString = int(s[l:r])
                output.append(s[r + 1:(lengthOfString + r + 1)])
                r += lengthOfString
                l = r + 1
            r += 1
        return output