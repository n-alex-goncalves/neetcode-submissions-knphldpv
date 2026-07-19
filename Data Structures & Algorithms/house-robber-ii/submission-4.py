class Solution:
    def standardRob(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        table = [0] * len(nums)
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            table[i] = max(table[i - 1], table[i - 2] + nums[i])
        
        print(table)
        return table[-1]

    def rob(self, nums: List[int]) -> int:
        print(nums[2:-1], nums[0])
        print(nums[1:])
        return max(
            self.standardRob(nums[2:-1]) + nums[0],
            self.standardRob(nums[1:])
        )