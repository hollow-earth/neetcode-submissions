class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l_ptr = 0
        r_ptr = len(heights)-1

        while l_ptr < r_ptr:
            max_water = max(max_water, min(heights[r_ptr], heights[l_ptr]) * (r_ptr - l_ptr))

            if heights[l_ptr] >= heights[r_ptr]:
                r_ptr -= 1
            else:
                l_ptr += 1
        
        return max_water
            