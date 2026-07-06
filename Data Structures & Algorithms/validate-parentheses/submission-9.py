class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        for character in s:
            if character in dictionary:
                stack.append(dictionary[character])
            elif stack and stack[-1] == character:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
        