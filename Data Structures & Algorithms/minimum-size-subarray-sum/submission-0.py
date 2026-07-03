class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Dynamic sliding window problem
        l_ptr, r_ptr = 0,0
        min_length = 999999
        
        while r_ptr < len(nums):
            if sum(nums[l_ptr:r_ptr+1]) >= target:
                min_length = min(min_length, len(nums[l_ptr:r_ptr+1]))
                l_ptr += 1
            else:
                r_ptr += 1
        return 0 if min_length == 999999 else min_length