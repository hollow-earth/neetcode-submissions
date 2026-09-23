class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lptr, rptr = 0, len(nums) - 1
        k = len(nums)

        while lptr <= rptr:
            if nums[lptr] == val:
                _tmp = nums[lptr]
                nums[lptr] = nums[rptr]
                nums[rptr] = _tmp
                rptr -= 1
                k -= 1
            else:
                lptr += 1
        return k