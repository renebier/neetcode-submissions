class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base_mp = {}
        for s in s1:
            base_mp[s] = base_mp.get(s,0)+1
        l=0
        mp = base_mp.copy()
        for r in range(len(s2)):
            c = s2[r]
            if c in mp:
                mp[c] -= 1
                if mp[c] < 0:
                    while l<r:
                        if s2[l] in mp:
                            mp[s2[l]] +=1
                        if s2[l] == c:
                            break
                        l+=1

            else:
                l=r+1
                mp = base_mp.copy()
            if all([True if val == 0 else False for val in mp.values()]):
                return True
            
        return False

        