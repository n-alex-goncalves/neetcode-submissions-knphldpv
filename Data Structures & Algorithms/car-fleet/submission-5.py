class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [((target - p) / s, p) for p, s in zip(position, speed)]
        stack = []
        
        time = sorted(time, key=lambda x:x[1])
        for t, p in time:
            while stack and stack[-1][0] <= t:
                stack.pop()
            stack.append((t, p))
        return len(stack)

        