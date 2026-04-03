class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        for character in s:
            if character in dictionary:
                stack.append(dictionary[character])
            elif len(stack) == 0 or stack.pop() != character:
                return False
        
        return len(stack) == 0
        