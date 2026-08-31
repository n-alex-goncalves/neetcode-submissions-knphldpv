class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.cur = []
        self.output = []

        def backtrack(i):
            if (
                i == len(nums)
            ):
                self.output.append(self.cur.copy())
                return
            
            self.cur.append(nums[i])

            backtrack(i + 1)

            self.cur.pop()

            backtrack(i + 1)

        backtrack(0)
        print(self.output)
        return self.output

        