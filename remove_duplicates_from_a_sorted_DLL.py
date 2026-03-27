def removeDuplicates(head):
    if not head:
        return head

    current = head
    while current and current.next:
        if current.data == current.next.data:
            dup = current.next
            current.next = dup.next
            if dup.next:
                dup.next.prev = current
            dup = None   
        else:
            current = current.next

    return head