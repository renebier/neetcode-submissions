class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        # find smallest element index
        while l < r:
            mid = l+ (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        if nums[l] <= target <= nums[-1]:
            l = r
            r = len(nums) - 1
        else:
            l = 0
            r = r - 1

        while l<=r:
            m = l+(r-l) //2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
