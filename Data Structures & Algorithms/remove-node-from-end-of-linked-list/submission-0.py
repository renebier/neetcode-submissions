# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        for _ in range(n):
            node = node.next
        dummy = ListNode(0,head)
        left = dummy
        while node:
            left = left.next
            node = node.next
        left.next = left.next.next
        return dummy.next
