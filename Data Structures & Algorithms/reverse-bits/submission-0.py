class Solution:
    def reverseBits(self, n: int) -> int:
        lst = str(bin(n))[2:]
        lst = '0' * (32 - len(lst)) + lst
        output = 0
        for i in range(32):
            if lst[i] == '1':
                output += 2 ** i
        return output
        