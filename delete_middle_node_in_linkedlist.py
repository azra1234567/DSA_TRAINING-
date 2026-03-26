class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete slow (middle)
        prev.next = slow.next
        return head