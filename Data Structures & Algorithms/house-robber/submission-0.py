class Solution:
    def rob(self, nums: List[int]) -> int:
        # TABULATION
        table = [0] * (len(nums) + 2)

        for i in range(len(nums) - 1, -1, -1):
            table[i] = max(nums[i] + table[i + 2], table[i + 1])
        
        print(table)
        return table[0]

        