class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0

        for num in nums:
            seen.add(num)
        
        for num in nums:
            seq_start = num - 1 not in seen
            if not seq_start:
                continue
            length = 1
            while num + length in seen:
                length += 1
            longest = max(length, longest)
        return longest