class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        self.currentList = []

        def isPalindrome(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        def backtrack(i):
            if i == len(s):
                self.output.append(self.currentList.copy())
                return
            currentString = ""
            for j in range(i, len(s)):
                currentString += s[j]
                if isPalindrome(currentString):
                    self.currentList.append(currentString)
                    backtrack(j + 1)
                    self.currentList.pop()
            return
        
        backtrack(0)
        return self.output

                
        