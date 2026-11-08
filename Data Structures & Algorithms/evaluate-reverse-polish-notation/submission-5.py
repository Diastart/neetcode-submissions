class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    stack.append(val1 + val2)
                elif token == '-':
                    stack.append(val1 - val2)
                elif token == '*':
                    stack.append(val1 * val2)
                elif token == '/':
                    val = abs(val1) // abs(val2)
                    if (val1 < 0) != (val2 < 0):
                        val = -val
                    stack.append(val)
            else:
                stack.append(int(token))
        return stack[-1]
                