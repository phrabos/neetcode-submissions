class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        pref_prod = 1
        suff_prod = 1

        for i in range(n):
            pref[i] = pref_prod
            pref_prod *= nums[i]
        
        for j in range(n -1, -1, -1):
            suff[j] = suff_prod
            suff_prod *= nums[j]

        res = [1] * n
        for k in range(n):
            res[k] = pref[k] * suff[k]
        return res