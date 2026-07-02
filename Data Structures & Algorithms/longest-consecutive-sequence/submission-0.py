class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for i in nums:
            if i-1 not in num_set:
                streak = 0
                while i in num_set:
                    streak += 1
                    i += 1
                longest = max(streak, longest)

        return longest
