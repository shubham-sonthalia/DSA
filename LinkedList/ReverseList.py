class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            t = cur.next 
            cur.next = prev
            prev = cur
            cur = t 
        return prev
