class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, _ in enumerate(nums):
            if nums[idx] > 0:
                break
            if idx > 0 and nums[idx-1] == nums[idx]:
                continue
            
            l_ptr = idx + 1
            r_ptr = len(nums) - 1

            while l_ptr < r_ptr:
                current_res = nums[idx] + nums[l_ptr] + nums[r_ptr]
                if current_res > 0:
                    r_ptr -= 1
                elif current_res < 0:
                    l_ptr += 1
                else:
                    res.append([nums[idx], nums[l_ptr], nums[r_ptr]])
                    r_ptr -= 1
                    l_ptr += 1

                    print(r_ptr, l_ptr)
                    while l_ptr < r_ptr and nums[r_ptr] == nums[r_ptr+1]:
                        r_ptr -= 1

        return res