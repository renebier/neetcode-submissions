class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        capacity = 0
        l = 0
        while l < len(height):
            if height[l] > 0:
                r = l + 1
                best_r = -1
                while r < len(height):
                    if height[r] >= height[l]:
                        best_r = r
                        break
                    if best_r == -1 or height[r] > height[best_r]:
                        best_r = r
                    r += 1
                
                if best_r != -1:
                    hl, hr = height[l], height[best_r]
                    h = min(hl, hr)
                    for i in range(l + 1, best_r):
                        capacity += max(0, h - height[i])
                    l = best_r
                else:
                    l += 1
            else:
                l += 1
        return capacity