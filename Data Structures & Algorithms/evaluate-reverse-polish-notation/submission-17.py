class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '/':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    stack.append(int(operand2 / operand1))
                case '*':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    stack.append(operand1 * operand2)
                case '+':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    stack.append(operand1 + operand2)
                case '-':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    stack.append(operand2 - operand1)
                case _:
                    stack.append(int(token))
        return stack[-1]
            
            
            