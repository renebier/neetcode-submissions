class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if nums[i] in m.values():
                j = [key for key, val in m.items() if val == nums[i]]
                return[j.pop(),i]
            m[i] = target - nums[i]
            
        return []