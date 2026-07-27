class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        memoization
        tabulation

        memo

        if i in memo
        if i >= len(nums)

        for j in range(i, len(nums)):
            if nums[i] < nums[j]:
                dp(conintune + 1)

        how can i tell the difference between 2D and 1D
        '''

        def dp(i, total, memo={}):
            if i in memo:
                return memo[i]
            if i == len(nums):
                return total + 1
            
            maxLength = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    maxLength = max(maxLength, dp(j, total) + 1)
            
            memo[i] = maxLength
            return memo[i]
        
        maxLength = 0
        for i in range(len(nums)):
            maxLength = max(maxLength, dp(i, 0))
        return maxLength
            