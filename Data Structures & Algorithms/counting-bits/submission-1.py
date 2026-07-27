class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            output.append(sum([int(x) for x in f"{i:08b}"]))
        return output