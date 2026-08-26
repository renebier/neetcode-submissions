class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n  = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            n[i] = prefix
            prefix *= num
        postfix = 1
        for i in reversed(range(len(nums))):
            n[i] *= postfix
            postfix *= nums[i]
        return n