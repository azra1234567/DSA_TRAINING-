class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        #  Find length and tail
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        #Make it circular
        tail.next = head

        #  Adjust k
        k = k % length
        steps_to_new_tail = length - k

        #Find the new tail
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # New head and break the link
        new_head = new_tail.next
        new_tail.next = None

        return new_head