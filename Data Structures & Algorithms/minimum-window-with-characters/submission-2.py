from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""
            
        countT = Counter(t)
        need = len(countT.keys())
        have = 0
        
        min_len = float("inf")
        res_range = (0, 0)
        l = 0
        
        for r in range(len(s)):
            char_r = s[r]
            if char_r in countT:
                countT[char_r] -= 1
                if countT[char_r] == 0:
                    have += 1
                
            # Sobald alle benötigten Zeichen im Fenster sind
            while have == need:
                # Kürzestes Fenster aktualisieren
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res_range = (l, r + 1)
                    
                # Linken Rand nach rechts schieben und Map aktualisieren
                char_l = s[l]
                if char_l in countT:
                    countT[char_l] += 1
                    if countT[char_l] == 1:
                        have -= 1
                l += 1
                
        return s[res_range[0]:res_range[1]] if min_len != float("inf") else ""