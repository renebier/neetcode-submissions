class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_biggest = (0,0)
        b_area = 0
        l = 0
        r = len(heights)-1
        while l<r:
            hr=heights[r]
            hl=heights[l]
            area = (r-l) * min(hl, hr)
            if area > b_area:
                b_area = area
                current_biggest = (l,r)
            if hl > hr:
                r -= 1
            else:
                l += 1
        return b_area