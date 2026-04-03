import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in dictionary:
                return [dictionary[target - num], i]
            dictionary[num] = i
        
        return [-1, -1]