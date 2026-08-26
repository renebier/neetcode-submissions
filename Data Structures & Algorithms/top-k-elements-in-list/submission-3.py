class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums) +1)]
        for n in nums:
            d[n] = d.get(n, 0) + 1
        out = list()
        for key, val in d.items():
            freq[val].append(key)
        i = 0
        for l in reversed(freq):
           for n in l:
            out.append(n)
            i += 1
            if i>=k:
                return out
        return out