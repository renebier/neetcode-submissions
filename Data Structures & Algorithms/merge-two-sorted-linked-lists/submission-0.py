# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = 0
        prev = 0
        if not list1:
            return list2
        elif not list2:
            return list1 
        elif list1.val < list2.val:
            root = list1
            list1 = list1.next
        else:
            root = list2
            list2 = list2.next
        prev = root
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next
        if not list1:
            prev.next = list2
            return root
        else:
            prev.next = list1
            return root