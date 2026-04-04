class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lst = [False] * len(nums)
        lst[0] = True
        for i, num in enumerate(nums):
            if lst[i]:
                j = i
                while j < len(nums) and j < i + num + 1:
                    lst[j] = True
                    j += 1
            if lst[-1]:
                return True
        return lst[-1]

        