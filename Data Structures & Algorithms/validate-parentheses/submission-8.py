class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for b in s:
            if b not in close_to_open:
                stack.append(b)
            else:
                if not stack:
                    return False
                last = stack[-1]
                if last == close_to_open[b]:
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False
