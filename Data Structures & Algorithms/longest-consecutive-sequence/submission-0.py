class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current_longest = 0
        i,j = 0,1
        s = set(nums)
        for num in nums:
            if num-1 in s:
                continue
            temp_longest = 0
            while num in s:
                temp_longest += 1
                num += 1
            if temp_longest > current_longest:
                current_longest = temp_longest
        return current_longest
        