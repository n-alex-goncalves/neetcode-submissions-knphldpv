class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        i = 0
        while i < len(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1  
                elif cur < 0:
                    l += 1
                else:
                    r -= 1
            
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            
        return output