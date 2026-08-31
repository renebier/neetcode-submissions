class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top = len(nums)-1
        bottom = 0
        while bottom <= top:
            middle = bottom + int((top-bottom) /2)
            n = nums[middle]
            if n == target:
                return middle
            elif n > target: 
                top = middle-1
            else:
                bottom = middle+1
        return -1
            