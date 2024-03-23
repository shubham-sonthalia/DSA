lass Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        nextNode = slow.next 
        slow.next = None
        def reverseList(head):
            cur = head
            prev = None
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        reversedList = reverseList(nextNode)

        finalHead = head
        finalTail = head
        flag = False

        cur1 = head.next 
        cur2 = reversedList
        while cur1 and cur2:
            if not flag:
                finalTail.next = cur2
                cur2 = cur2.next
                finalTail = finalTail.next
            else:
                finalTail.next = cur1
                cur1 = cur1.next
                finalTail = finalTail.next
            flag = not flag 
        while cur1: 
            finalTail.next = cur1
            cur1 = cur1.next
            finalTail = finalTail.next
        while cur2:
            finalTail.next = cur2
            cur2 = cur2.next
            finalTail = finalTail.next
        return finalHead
