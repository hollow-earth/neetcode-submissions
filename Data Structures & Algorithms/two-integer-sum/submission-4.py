class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = defaultdict(int)
        for index, i in enumerate(nums):
            if target - i not in ans:
                ans[i] = index
            else:
                return sorted([index, ans[target - i]])