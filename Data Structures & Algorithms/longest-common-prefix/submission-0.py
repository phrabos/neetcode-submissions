class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")

        for w in strs:
            min_length = min(min_length, len(w))
        print('min', min_length)        
        i = 0
        while i < min_length:
            for s in strs:
                curr_char = s[i]
                anchor_char = strs[0][i]
                if curr_char != anchor_char:
                    return s[:i]
            i += 1
        return strs[0][:i]