class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Mitte finden (slow landet genau auf der Mitte)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Zweite Hälfte isolieren und umdrehen
        curr = slow.next
        slow.next = None  # WICHTIG: Erste Hälfte sauber terminieren
        
        prev = None       # WICHTIG: Muss None sein, damit kein Zyklus entsteht
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Erste Hälfte (head) und umgedrehte zweite Hälfte (prev) verweben
        first = head
        second = prev     # prev ist der Kopf der umgedrehten zweiten Hälfte
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2