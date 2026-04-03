class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - p) / s for p, s in sorted(zip(position, speed))]
        stack = []

        for t in times:
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        
        return len(stack)
        