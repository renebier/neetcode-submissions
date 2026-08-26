class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for num in s:
            if num-1 in s:
                continue
            temp_longest = 0
            while num in s:
                temp_longest += 1
                num += 1
            longest = max(longest,temp_longest)
        return longest
        