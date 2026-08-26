class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l<r:
            diff = target - numbers[l] - numbers[r]
            if diff < 0:
                r-=1
                continue
            elif diff > 0:
                l+=1
                continue
            return [l+1,r+1]
        return []