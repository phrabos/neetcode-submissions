class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        
        if not nums:
            return res
        
        i = 0
        while i < len(nums):
            start = nums[i] # start of a sequence
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if nums[i] != start:
                res.append(str(start)+"->"+str(nums[i]))
            else:
                res.append(str(nums[i]))

        return res