class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = []

        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for c in s:
            if c in bracket_map:
                stack.append(c)
            else:
                if len(stack) != 0 and bracket_map[stack[-1]] == c:
                    stack.pop(-1)
                    continue
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True

        