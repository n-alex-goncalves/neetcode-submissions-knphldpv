class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            target, l, r = -1 * num, i + 1, len(nums) - 1
            while l < r:
                if (nums[l] + nums[r]) < target:
                    l += 1
                elif (nums[l] + nums[r]) > target:
                    r -= 1
                else:
                    output.append([nums[l], nums[r], num])
                    r -= 1
                    while r > 0 and nums[r] == nums[r + 1]:
                        r -= 1

        return output       