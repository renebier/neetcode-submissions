import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r= max(piles)
        last_possible = 0
        while l <= r:
            k = l+(r-l) // 2
            time = h
            for pile in piles:
                time -= math.ceil(pile/k)

            if time < 0:
                l = k+1
            elif time >= 0:
                r = k-1
                last_possible = k
        return last_possible
            