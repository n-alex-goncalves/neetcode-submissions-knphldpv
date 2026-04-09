class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        backtracking
        sorted (?)
        skip consecutive

        add myself
        output
        continue

        first, see without duplicates
        '''
        self.output = []
        self.cur = []

        def backtrack(i):
            if i > len(nums):
                return

            self.output.append(self.cur.copy())
            
            for j in range(i, len(nums)):
                self.cur.append(nums[j])
                backtrack(j + 1)
                self.cur.pop()

        backtrack(0)
        return self.output
        