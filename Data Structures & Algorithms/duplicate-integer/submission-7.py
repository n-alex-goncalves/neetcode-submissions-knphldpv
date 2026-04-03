class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()
        for num in nums:
            if num in dictionary:
                return True
            dictionary[num] = True
        return False
        