class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.cur = []
        self.output = []
        def backtrack(total, i):
            if total < 0:
                return
            if total == 0:
                self.output.append(self.cur.copy())
                return
            
            for j in range(i, len(nums)):
                self.cur.append(nums[j])
                backtrack(total - nums[j], j)
                self.cur.pop()
            
        backtrack(target, 0)
        return self.output
