class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = set()
        for idx, i in enumerate(nums):
            if idx > k:
                res.remove(nums[idx-k-1])
            if i not in res:
                res.add(i)
            else:
                return True
        return False

        