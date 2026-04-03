class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        INPUT: list
        OUTPUT: single number

        two pointer / greedy / one pass

        while n + 1 exists
        '''
        unique = set(nums)
        maxLength = 0

        for number in unique:
            if number - 1 not in unique:
                curLength = 1
                cur = number + 1
                while cur in unique:
                    curLength += 1
                    cur += 1
                maxLength = max(maxLength, curLength)
        
        return maxLength
        