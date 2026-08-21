class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        operators = set(["+", "-", "*", "/"])

        for s in tokens:
            if s in operators:
                if s == "+":
                    res = stack.pop() + stack.pop()
                elif s == "-":
                    a, b = stack.pop(), stack.pop()
                    res = b - a 
                elif s == "*":
                    res = stack.pop() * stack.pop()
                else:
                    a, b = stack.pop(), stack.pop()
                    res = int(float(b) / a)
                stack.append(res)
            else:
                stack.append(int(s))
        return stack[0]
