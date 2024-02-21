class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0 
        cur = head
        while cur:
            l += 1
            cur = cur.next
        cur = head 
        for i in range(l//2):
            cur = cur.next 
        return cur
