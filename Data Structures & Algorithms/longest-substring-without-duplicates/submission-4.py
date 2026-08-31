class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        n = len(s)
        max_substring_len = 0

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_substring_len = max(max_substring_len, (r - l + 1))
        
        return max_substring_len