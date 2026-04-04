class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        output = nums[0]
        for i, num in enumerate(nums):
            if total < 0:
                total = 0
            total += num
            output = max(output, total)
        return output
        