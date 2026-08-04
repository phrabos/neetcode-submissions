class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # count_s, count_t = {}, {}

        # for i in range(len(s)):
        #     count_s[s[i]] = count_s.get(s[i], 0) + 1
        #     count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        # return count_s == count_t

        char_count = [0] * 26
        for i in range(len(s)):
            s_idx = ord(s[i]) - ord("a")
            t_idx = ord(t[i]) - ord("a")
            char_count[s_idx] += 1
            char_count[t_idx] -= 1
        
        for cnt in char_count:
            if cnt > 0:
                return False
        return True