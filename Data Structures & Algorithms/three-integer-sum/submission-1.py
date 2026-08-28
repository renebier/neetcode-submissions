class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        possible = []
        nums.sort()
        for i, num in enumerate(nums):
            l = i+1
            r = len(nums)-1
            target = num
            while l<r:
                vals = - nums[l] - nums[r]
                if vals < target:
                    r-=1
                elif vals > target:
                    l+=1
                elif vals == target:
                    pair = [num,nums[l],nums[r]]
                    if not pair in possible:
                        possible.append([num,nums[l],nums[r]])
                    diffL = nums[l+1] - nums[l]
                    diffR = nums[r] - nums[r-1]
                    if diffL > diffR:
                        r-=1
                    else:
                        l+=1
        return possible