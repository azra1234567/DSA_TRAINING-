def removeDuplicates(head):
    if not head:
        return head

    current = head

    while current and current.next:
        if current.data == current.next.data:
            # Node to delete
            dup = current.next

            # Connect current to dup.next
            current.next = dup.next

            # Fix prev pointer if next exists
            if dup.next:
                dup.next.prev = current

            # free dup (optional in Python)
            dup = None
        else:
            current = current.next

    return head