import collections

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = collections.defaultdict(int)
        for num in nums:
            if num in dictionary:
                return True
            dictionary[num] = True

        return False 
         