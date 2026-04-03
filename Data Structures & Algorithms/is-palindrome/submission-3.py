class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [character.lower() for character in s if character.isalnum()]
        return all([lst[i] == lst[len(lst) - i - 1] for i in range(len(lst))])
        