class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(numbers):
            missing = target-num
            if missing in d:
                return [d[missing]+1,i+1]
            d[num] = i
        
        return []