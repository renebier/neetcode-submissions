class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        current_best = 0
        while r < len(prices):
            left = prices[l]
            right = prices[r]
            if left > right:
                l=r
            r +=1
            if right-left > current_best:
                current_best = right-left
        return current_best