class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = defaultdict(int)
        for i in nums:
            if c[i] == 0:
                c[i] += 1
            else:
                return True
        return False
        