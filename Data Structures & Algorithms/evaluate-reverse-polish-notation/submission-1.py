class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '*', '-', '/']
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right = stack.pop(-1)
                left = stack.pop(-1)
                if token == '+':
                    new = left + right
                    stack.append(new)
                elif token == '*':
                    new = left * right
                    stack.append(new)
                elif token == '-':
                    new = left - right
                    stack.append(new)
                else:
                    new = int(left / right)
                    stack.append(new)     

        return stack[0]   