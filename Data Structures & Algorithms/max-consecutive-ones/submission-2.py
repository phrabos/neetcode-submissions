class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0

        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            max_cnt = max(max_cnt, cnt)
        return max_cnt