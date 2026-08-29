class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base_mp = {}
        for s in s1:
            base_mp[s] = base_mp.get(s, 0) + 1
            
        l = 0
        mp = base_mp.copy()
        
        for r in range(len(s2)):
            c = s2[r]
            if c in mp:
                mp[c] -= 1
                while mp[c] < 0:
                    mp[s2[l]] += 1
                    l += 1
            else:
                l = r + 1
                mp = base_mp.copy()
                
            # Wenn das Fenster exakt die Länge von s1 hat und alle Werte 0 sind
            if r - l + 1 == len(s1):
                return True
                
        return False