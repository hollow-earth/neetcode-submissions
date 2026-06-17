class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for j,i in enumerate(nums):
            left_product, right_product = 1,1
            for k in range(0,j):
                left_product *= nums[k]
            for k in range(len(nums)-1, j,-1):
                right_product *= nums[k]
            res[j] = right_product * left_product
        return res