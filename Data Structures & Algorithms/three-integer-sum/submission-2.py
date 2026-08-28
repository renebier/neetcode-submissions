class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Optimierung: Da das Array sortiert ist, kann eine Summe mit Startwert > 0 nie 0 ergeben
            if nums[i] > 0:
                break
                
            # Duplikate für das erste Element überspringen
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Duplikate für das zweite und dritte Element überspringen
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
        return res