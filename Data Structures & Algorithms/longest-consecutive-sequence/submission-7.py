class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLength = 0
        for num in nums:
            length = 1
            cur = num
            while cur + 1 in nums:
                length += 1
                cur += 1
            maxLength = max(length, maxLength)
        return maxLength