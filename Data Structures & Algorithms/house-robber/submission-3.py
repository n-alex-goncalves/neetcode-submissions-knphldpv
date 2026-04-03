class Solution:
    def rob(self, nums: List[int]) -> int:


        def robHouse(index, money, memo=dict()):
            if index >= len(nums):
                return money
            if index in memo:
                return memo[index]
            
            memo[index] = max(
                robHouse(index + 1, money), 
                robHouse(index + 2, money) + nums[index]
            )
            return memo[index]

        return robHouse(0, 0)

        