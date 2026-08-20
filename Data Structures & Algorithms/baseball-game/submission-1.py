class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for i, op in enumerate(operations):
            print('score', score)
            if op == "+":
                new_score = score[-1] + score[-2]
                score.append(new_score)
            elif op == "C":
                score.pop()
            elif op == "D":
                double = score[-1] * 2
                score.append(double)
            else:
                score.append(int(op))
            
        return sum(score)
            