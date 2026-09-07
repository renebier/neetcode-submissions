"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = defaultdict(lambda:Node(0))
        d[None] = None
        l = head
        while l:
            d[l].val = l.val
            d[l].random = d[l.random]
            d[l].next = d[l.next]
            l = l.next
        return d[head]
