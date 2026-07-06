class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [character.lower() for character in s if character.isalnum()]
        length = len(lst) - 1
        return all([lst[i] == lst[len(lst) - 1 - i] for i in range(len(lst) // 2)])
        