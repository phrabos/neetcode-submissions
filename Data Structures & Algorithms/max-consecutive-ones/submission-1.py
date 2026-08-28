class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_count = 0

        for num in nums:
            if num == 0:
                cnt = 0
            else:
                cnt += 1
            max_count = max(max_count, cnt) 
        
        return max_count