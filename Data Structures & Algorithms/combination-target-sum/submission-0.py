class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.cur = []
        def backtrack(total, i, cur):
            if (
                total > target or
                i >= len(nums)
            ):
                return
            
            if total == target:
                self.output.append(cur)
            
            for j, num in enumerate(nums[i:], start=i):
                backtrack(total + num, j, cur + [num])

        backtrack(0, 0, [])
        return self.output
