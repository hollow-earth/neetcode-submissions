class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            totaltime = 0
            m = ( l + r ) // 2
            for p in piles:
                totaltime += math.ceil(float(p)/float(m))
            if totaltime <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
