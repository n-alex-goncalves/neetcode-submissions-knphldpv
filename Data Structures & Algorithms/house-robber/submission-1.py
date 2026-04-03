class Solution:
    def rob(self, nums: List[int]) -> int:
        # MEMOIZATION
        def robHouses(index, money, memo=dict()):
            if index in memo:
                return memo[index] 
            if index >= len(nums):
                return money
        
            memo[index] = max(
                robHouses(index + 1, money),
                nums[index] + robHouses(index + 2, money)
            )
            return memo[index]
        
        return robHouses(0, 0)

        