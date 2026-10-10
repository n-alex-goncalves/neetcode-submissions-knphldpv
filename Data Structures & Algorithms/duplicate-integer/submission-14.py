class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        input: nums
        output: boolean
        solution: take in nums, dictionary, return true if in dictionary
        '''
        dictionary = dict()
        for num in nums:
            if num in dictionary:
                return True
            else:
                dictionary[num] = num
                
        return False
        