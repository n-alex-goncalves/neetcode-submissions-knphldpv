class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = [[]]
        self.cur = []

        def backtrack(i):
            if (
                i == len(nums)
            ):
                self.output.append(self.cur.copy())
                return

            self.cur.append(nums[i])

            for j in range(i + 1, len(nums) + 1):
                backtrack(j)

            self.cur.pop()

            return
        
        for i in range(len(nums)):
            backtrack(i)

        return self.output