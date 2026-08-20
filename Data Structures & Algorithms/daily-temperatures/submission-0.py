class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                tup_t, tup_i = stack.pop()
                res[tup_i] = i - tup_i
            stack.append((t, i))
        return res