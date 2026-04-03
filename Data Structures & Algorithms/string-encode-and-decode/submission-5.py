import random

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for string in strs:
            output.extend([str(len(string)), "#", string])
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output, l, r = [], 0, 0
        while r < len(s):
            character = s[r]
            if character == "#":
                lenOfChar = int(s[l:r])
                output.append( s[r+1:r+lenOfChar+1])
                l = r = r + lenOfChar + 1
            else:
                r += 1
        return output
