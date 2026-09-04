def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if is_integer(token):
                stack.append(int(token))
            elif token == '+':
                second, first = stack.pop(), stack.pop()
                stack.append(first + second)
            elif token == '*':
                second, first = stack.pop(), stack.pop()
                stack.append(first * second)
            elif token == '-':
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif token == '/':
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))
        return stack[0]

        