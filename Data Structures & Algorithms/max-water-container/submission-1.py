class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            min_height = min(heights[l], heights[r])
            width = r - l
            curr_water = min_height * width
            most_water = max(curr_water, most_water)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return most_water