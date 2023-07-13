class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}',
                    '(': ')',
                    '[': ']'
                   }
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue
            last = stack[-1]
            if last in brackets.keys():
                if brackets[last] == c:
                    stack.pop()
                    continue
            stack.append(c)
        
        return len(stack) == 0