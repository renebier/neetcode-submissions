class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in mp.values():
                stack.append(c)
            elif c in mp.keys():
                if not stack or stack.pop() != mp[c]:
                    return False
        if not stack:
            return True
        return False