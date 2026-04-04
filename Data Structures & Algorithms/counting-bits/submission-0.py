class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            return sum(int(x) for x in str(bin(n))[2:])
        output = []
        for i in range(n + 1):
            output.append(count(i))
        return output
        