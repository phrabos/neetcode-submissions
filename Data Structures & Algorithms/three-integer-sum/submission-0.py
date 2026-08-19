class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n -2):
            curr = nums[i]
            l, r = i + 1, n - 1
            if curr > 0:
                return res
            if i > 0 and curr == nums[i - 1]:
                continue
            while l < r:
                if curr + nums[l] + nums[r] > 0:
                    r -= 1
                elif curr + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res