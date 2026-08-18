class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)

        for n in nums:
            num_count[n] += 1
            if num_count[n] > len(nums) // 2:
                return n
            