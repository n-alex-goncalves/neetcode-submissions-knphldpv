class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for character in s:
            if character in dictionary:
                stack.append(dictionary[character])
            elif stack and stack.pop() == character:
                continue
            else:
                return False
        
        return len(stack) == 0