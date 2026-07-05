class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("inf")
        maxP = 0

        for i in range(len(prices)):
            low = min (low, prices[i])
            maxP = max(maxP, prices[i] - low)
        return maxP
