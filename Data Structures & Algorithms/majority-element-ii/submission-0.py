class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)
        res = []

        for i in nums:
            hm[i] += 1
        
        for j in hm.keys():
            if hm[j] > len(nums) // 3:
                res.append(j)
        return res

        