class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            cur, j = None, None
            while stack and temp >= stack[-1][0]:
                stack.pop()
            output[i] = stack[-1][1] - i if stack else 0
            stack.append((temp, i))
        return output

        