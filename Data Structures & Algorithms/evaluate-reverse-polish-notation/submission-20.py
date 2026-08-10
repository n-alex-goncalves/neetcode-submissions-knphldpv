class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            match x:
                case "+":
                    operand1, operand2 = stack.pop(), stack.pop()
                    stack.append(operand1 + operand2)
                case "*":
                    operand1, operand2 = stack.pop(), stack.pop()
                    stack.append(operand1 * operand2)
                case "-":
                    operand1, operand2 = stack.pop(), stack.pop()
                    stack.append(operand2 - operand1)
                case "/":
                    operand1, operand2 = stack.pop(), stack.pop()
                    stack.append(int(operand2 / operand1))
                case _:
                    stack.append(int(x))
        return stack[-1]

            
        