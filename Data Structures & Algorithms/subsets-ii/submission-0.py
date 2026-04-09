class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        backtrack
        
        sorted (?)
        skip consecutive
        
        '''
        self.output = []
        self.cur = []
    
        def backtrack(i):
            if i >= len(nums):
                self.output.append(self.cur.copy())
                return 
            
            self.cur.append(nums[i])
            backtrack(i + 1)
            self.cur.pop()

            j = i + 1
            while j < len(nums) and nums[j - 1] == nums[j]:
                j += 1
            backtrack(j)
        
        nums = sorted(nums)
        backtrack(0)
        return self.output