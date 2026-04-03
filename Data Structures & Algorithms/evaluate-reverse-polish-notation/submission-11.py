class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == '+':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand2 + operand1)
            elif token == '*':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand2 * operand1)
            elif token == '-':
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand2 - operand1)
            elif token == '/':
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(int(operand2 / operand1))
            else:
                stack.append(int(token))
        return stack[-1]