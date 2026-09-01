class Solution:
    def search(self, nums: List[int], target: int) -> int:
                # At any mid point, ONE side is always sorted
        # Check which side is sorted, then check if target is in that sorted side
        l = 0
        r = len(nums) - 1 
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            
            # left side is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:  # target in sorted left side
                    r = mid - 1
                else:
                    l = mid + 1
            # right side is sorted
            else:
                if nums[mid] < target <= nums[r]:  # target in sorted right side
                    l = mid + 1
                else:
                    r = mid - 1
        return -1