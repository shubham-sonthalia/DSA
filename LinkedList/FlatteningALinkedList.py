def flatten(root):
    def merge(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        finalHead = l1 
        finalTail = l1 
        if l1.data < l2.data:
            finalHead = l1
            finalTail = l1
            l1 = l1.bottom
        else:
            finalHead = l2
            finalTail = l2
            l2 = l2.bottom
        while l1 and l2:
            if l1.data < l2.data:
                finalTail.bottom = l1
                finalTail = finalTail.bottom
                l1 = l1.bottom
            else:
                finalTail.bottom = l2
                finalTail = finalTail.bottom
                l2 = l2.bottom
        while l1:
            finalTail.bottom = l1
            finalTail = finalTail.bottom
            l1 = l1.bottom
        while l2:
            finalTail.bottom = l2
            finalTail = finalTail.bottom
            l2 = l2.bottom
        return finalHead
    ptr1 = root
    ptr2 = root.next
    while ptr2:
        ptr1 = merge(ptr1, ptr2)
        ptr2 = ptr2.next
    return ptr1
