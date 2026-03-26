

def lengthOfLoop(head):
    slow = fast = head

    # Step 1: Detect the cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # loop found
            return count_loop_nodes(slow)

    return 0  # no loop


def count_loop_nodes(meeting_point):
    count = 1
    temp = meeting_point.next

    while temp != meeting_point:
        count += 1
        temp = temp.next

    return count