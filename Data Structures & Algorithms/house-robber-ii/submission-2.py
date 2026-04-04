class Solution:
    def rob(self, nums: List[int]) -> int:
        def robSplit(nums):
            table = [0] * (len(nums) + 2)
            for i in range(len(nums) - 1, -1, -1):
                table[i] = max(nums[i] + table[i + 2], table[i + 1])
            return table[0]
        
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]

        return max(robSplit(nums1), robSplit(nums2))