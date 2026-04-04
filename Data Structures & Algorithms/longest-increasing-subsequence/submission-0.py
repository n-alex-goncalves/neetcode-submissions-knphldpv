class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    table[i] = max(table[i], table[j] + 1)
        return max(table)
        
        