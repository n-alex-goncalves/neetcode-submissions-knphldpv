class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        table = [0] * (len(cost) + 2)

        for i in range(len(cost) - 1, -1, -1):
            table[i] += cost[i] + min(table[i + 1], table[i + 2])
        
        return min(table[0], table[1])