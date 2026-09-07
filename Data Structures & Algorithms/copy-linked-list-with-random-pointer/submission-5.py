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
        if head is None:
            return None
        l1 = head
        while l1:
            l1.random = Node(l1.val, l1.random,None)
            l1 = l1.next
        
        l1 = head
        newHead = l1.random
        while l1:
            rand = l1.random.next
            l1.random.random = rand.random if rand else None
            l1 = l1.next
        l1 = head
        while l1:
            new = l1.random
            l1.random = new.next
            new.next = l1.next.random if l1.next else None
            l1 = l1.next

        return newHead