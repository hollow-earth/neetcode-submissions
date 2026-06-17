class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = defaultdict(int)
        for i,j in enumerate(nums):
            _j = target - j
            if _j not in res.keys():
                res[j] = i
            else:
                return [res[_j], i]