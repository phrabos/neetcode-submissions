class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt_zeros = 0
        max_cnt = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                cnt_zeros += 1
            while cnt_zeros > 1:
                if nums[l] == 0:
                    cnt_zeros -= 1
                l += 1
            max_cnt = max(max_cnt, r - l + 1)


        return max_cnt