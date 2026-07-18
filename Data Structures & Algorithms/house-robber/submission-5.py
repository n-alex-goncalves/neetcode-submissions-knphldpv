class Solution:
    def rob(self, nums: List[int]) -> int:
        def steal(i, memo={}):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
        
            memo[i] = max(
                nums[i] + steal(i + 2),
                steal(i + 1)
            )
            return memo[i]
        
        return steal(0)
        