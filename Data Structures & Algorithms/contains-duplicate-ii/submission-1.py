class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = set()
        for idx, i in enumerate(nums):
            if i not in res:
                res.add(i)
                if idx >= k:
                    res.remove(nums[idx-k])
            else:
                return True
        return False

        