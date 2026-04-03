class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.cur = []
        def backtrack(total, i):
            if (
                total > target or
                i >= len(nums)
            ):
                return
            
            if total == target:
                self.output.append(self.cur.copy())
            
            for j, num in enumerate(nums[i:], start=i):
                self.cur.append(num)
                backtrack(total + num, j)
                self.cur.pop()

        backtrack(0, 0)
        return self.output
