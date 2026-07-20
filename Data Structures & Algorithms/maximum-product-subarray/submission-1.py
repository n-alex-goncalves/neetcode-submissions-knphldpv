class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        1   -2  -5
    p   1   1   10
    n   1   -2  -5

        '''
        if len(nums) == 1:
            return nums[0]

        table = [[0 for _ in range(len(nums))] for _ in range(2)]

        table[0][0] = nums[0]
        table[1][0] = nums[0]

        for i in range(1, len(nums)):
            table[0][i] = max(
                nums[i] * table[0][i - 1],
                nums[i] * table[1][i - 1],
                nums[i]
            )
            table[1][i] = min(
                nums[i] * table[0][i - 1],
                nums[i] * table[1][i - 1],
                nums[i]
            )
        
        return max(table[0])
        
