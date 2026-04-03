class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        nums = set(nums)

        for num in nums:
            curNum = num
            if curNum - 1 not in nums:
                curLength = 1
                while curNum + 1 in nums:
                    curNum += 1
                    curLength += 1
                maxLength = max(curLength, maxLength)
        return maxLength

        