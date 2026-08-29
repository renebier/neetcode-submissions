class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_occ = 0
        mp = {}
        for r in range(len(s)):
            mp[s[r]] = 1+ mp.get(s[r],0)
            max_occ = max(max_occ, mp[s[r]])
            while (r-l-max_occ+1) > k:
                mp[s[l]] -= 1
                l+=1
            res = max(res,r-l+1 )
        return res