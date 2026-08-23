class Solution:
    def canJump(self, nums: List[int]) -> bool:
        table = [False for _ in range(len(nums))]
        table[0] = True

        for i in range(len(nums)):
            if table[i]:
                for j in range(nums[i] + 1):
                    if i + j < len(nums):
                        table[i + j] = True
        
        return table[-1]