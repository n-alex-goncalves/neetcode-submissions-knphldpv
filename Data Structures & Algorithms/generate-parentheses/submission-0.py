class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        self.cur = []

        def backtrack(open, close):
            if open == 0 and close == 0:
                self.output.append("".join(self.cur))
                return

            if open == close:
                self.cur.append("(")
                backtrack(open - 1, close)
                self.cur.pop()
                return
            
            if open > 0 and open < close:
                self.cur.append("(")
                backtrack(open - 1, close)
                self.cur.pop()

                self.cur.append(")")
                backtrack(open, close - 1)
                self.cur.pop()
                return
            
            if open == 0:
                self.cur.append(")")
                backtrack(open, close - 1)
                self.cur.pop()
                return

            # can only close if open exists
            # can only open if n times
            # if open == close, cannot close, only open

        backtrack(n, n)
        return self.output