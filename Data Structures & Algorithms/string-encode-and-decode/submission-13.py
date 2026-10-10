class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.extend([str(len(word)), '|', word])
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '|':
                j += 1
            length = int(s[i:j])
            
            output.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        
        return output