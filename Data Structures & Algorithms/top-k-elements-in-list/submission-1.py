class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        out = list()
        for x, num in enumerate(reversed(sorted(d, key=d.get))):
            if x >= k:
                break
            out.append(num)
        return out