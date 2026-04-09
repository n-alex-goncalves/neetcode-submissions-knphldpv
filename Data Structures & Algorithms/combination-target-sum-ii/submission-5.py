class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.cur = []
        candidates = sorted(candidates)

        def backtrack(i, total):
            if total < 0:
                return
            if total == 0:
                self.output.append(self.cur.copy())
                return
            if i >= len(candidates):
                return
            
            self.cur.append(candidates[i])
            backtrack(i + 1, total - candidates[i])
            self.cur.pop()
            
            j = i
            while j < len(candidates):
                j += 1
                while j < len(candidates) and candidates[j - 1] == candidates[j]:
                    j += 1
                if j < len(candidates):
                    self.cur.append(candidates[j])
                    backtrack(j + 1, total - candidates[j])
                    self.cur.pop()

            return
        
        backtrack(0, target)
        return self.output
            