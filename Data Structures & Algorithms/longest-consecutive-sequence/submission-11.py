class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                curr_streak = 1
                while num + curr_streak in num_set:
                    curr_streak += 1
                longest = max(longest, curr_streak)
        
        return longest 