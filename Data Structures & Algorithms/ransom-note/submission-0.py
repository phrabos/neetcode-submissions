class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_count = defaultdict(int)
        
        for c in magazine:
            m_count[c] += 1
        for ch in ransomNote:
            m_count[ch] -= 1
        for k in m_count:
            if m_count[k] < 0:
                return False
        return True