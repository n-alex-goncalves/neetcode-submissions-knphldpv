class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * (n + 3)
        table[0] = 1

        for i in range(n + 1):
            table[i + 1] += table[i]
            table[i + 2] += table[i]
        
        return table[n]