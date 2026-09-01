# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if not head:
            return None
        elif not head.next:
            return head
        while head:
            stack.append(head.val)
            head = head.next
        l = ListNode(val = stack.pop())
        last = l
        while stack:
            val = ListNode(val=stack.pop())
            last.next = val
            last = val
        return l



