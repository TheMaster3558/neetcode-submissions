class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif c in (')', ']', '}'):
                if not stack:
                    return False
                elif stack[-1] == '(' and c == ')' or stack[-1] == '[' and c == ']' or stack[-1] == '{' and c == '}':
                    stack.pop()    
                else:
                    return False
            else:
                return False

        return not bool(stack)
        