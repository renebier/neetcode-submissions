class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]

        for price in prices:
            maxP = max(maxP, price-buy)
            buy = min(buy, price)
        return maxP