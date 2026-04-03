class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival = [((target - p) / s) for p, s in sorted(zip(position, speed), key=lambda x:x[0])]
        stack = []

        print(arrival)

        for car in arrival:
            if len(stack) == 0 or stack[-1] > car:
                stack.append(car)
                continue

            while stack and stack[-1] <= car:
                stack.pop()
            
            stack.append(car)
        
        print(stack)
        return len(stack)
