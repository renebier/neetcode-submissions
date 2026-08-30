from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque()  # Speichert Indizes
        
        for r in range(len(nums)):
            # 1. Alle kleineren Werte von hinten entfernen (sie werden nie mehr Maximum)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            q.append(r)
            
            # 2. Altes Maximum vorne entfernen, falls es links aus dem Fenster gerutscht ist
            if q[0] < r - k + 1:
                q.popleft()
                
            # 3. Sobald das erste Fenster voll ist (ab Index k - 1), Maximum speichern
            if r >= k - 1:
                res.append(nums[q[0]])
                
        return res