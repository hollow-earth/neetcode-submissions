class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(list)

        for i in range(len(nums)):
            t = target - nums[i]
            if t in hm:
                return sorted([i, hm[t][0]])
            else:
                hm[nums[i]].append(i)
        