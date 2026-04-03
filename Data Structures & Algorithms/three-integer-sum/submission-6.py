class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        output = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    output.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return output
