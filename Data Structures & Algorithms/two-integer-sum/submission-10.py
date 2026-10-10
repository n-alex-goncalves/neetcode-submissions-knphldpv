class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        input: nums
        output: list of integers
        solution:

        index, so, dictionary, find sum
        '''
        dictionary = dict()
        for i, num in enumerate(nums):
            if target - num in dictionary:
                return [dictionary[target - num], i]
            dictionary[num] = i
        return -1