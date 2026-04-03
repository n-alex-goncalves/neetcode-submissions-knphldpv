class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack with indexes
        when we pop, update index with maths
        '''
        output = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                j, cur = stack.pop()
                output[j] = i - j
            stack.append((i, temp))
        return output
    