class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLength = 0
        for num in nums:
            if num - 1 not in nums:
                cur = num
                length = 0
                while cur in nums:
                    cur += 1
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength
        