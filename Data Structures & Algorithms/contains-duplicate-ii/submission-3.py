class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1. Make hashmap
        # 2. Add every number to the hashmap along with its index
        # 3. If len(hashmap key) >= 2 check if the difference is <= k
        #   3a. If yes return True
        #   3b. Otherwise continue

        hm = defaultdict(list)

        for idx, i in enumerate(nums):
            hm[i].append(idx)
            if len(hm[i]) >= 2:
                for j in range(len(hm[i])-1):
                    if hm[i][j+1] - hm[i][j] <= k:
                        return True
        return False