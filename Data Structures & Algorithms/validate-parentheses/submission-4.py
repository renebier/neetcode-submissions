class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in mp.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != mp[c]:
                    return False
        return not stack