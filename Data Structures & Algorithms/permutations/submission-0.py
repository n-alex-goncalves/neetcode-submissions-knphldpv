class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.cur = []
        self.curSet = set()

        def backtrack(i):
            if len(self.cur) > len(nums):
                return

            self.cur.append(nums[i])
            self.curSet.add(nums[i])

            if len(self.cur) == len(nums):
                self.output.append(self.cur.copy())
                self.cur.pop()
                self.curSet.remove(nums[i])
                return

            for j in range(len(nums)):
                if nums[j] in self.curSet:
                    continue
                backtrack(j)
            self.cur.pop()
            self.curSet.remove(nums[i])

        for i in range(len(nums)):
            backtrack(i)

        return self.output
                
            
        