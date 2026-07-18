class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        table = [0] * len(nums)
        table[-1] = nums[-1]
        table[-2] = max(nums[-2], nums[-1])
    
        for i in range(len(nums) - 3, -1, -1):
            table[i] = max(nums[i] + table[i + 2], table[i + 1])

        return table[0]

