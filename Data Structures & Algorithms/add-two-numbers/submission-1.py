# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0)
        new = newHead
        prev = None
        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + new.val - 10
            new.val = s if s >= 0 else s+10
            new.next = ListNode(1 if s >=0 else 0)
            prev = new
            new = new.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        prev.next = None if prev.next.val == 0 else prev.next
        return newHead
             