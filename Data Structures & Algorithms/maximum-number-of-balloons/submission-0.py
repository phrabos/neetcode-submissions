class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balloon"
        char_count = defaultdict(int)

        for c in text:
            if c in balloon:
                char_count[c] += 1
        if any(c not in char_count for c in balloon):
            return 0
        return min(
            char_count["b"],
            char_count["a"],
            char_count["l"] // 2,
            char_count["o"] //2,
            char_count["n"]
            )