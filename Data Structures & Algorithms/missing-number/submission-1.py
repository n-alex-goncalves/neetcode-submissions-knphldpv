class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        for i, n in enumerate(nums):
            x ^= i ^ n
        return x 