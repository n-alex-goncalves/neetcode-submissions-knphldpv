class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        negative array -> needs a max negative?
        positive array -> needs the max positive?

        multiple across and see?

        dp, so how does it break down into a  multiple subproblem.
        right two

        '''
        p = [1] * len(nums)
        n = [1] * len(nums)

        p[-1] = nums[-1]
        n[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            p[i] = max(nums[i] * p[i + 1], nums[i] * n[i + 1], nums[i])
            n[i] = min(nums[i] * n[i + 1], nums[i] * p[i + 1], nums[i])
        
        return max(p)
            