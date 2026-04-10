class Solution:
    def isPalindrome(self, head):

        #  find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #  reverse second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        #  compare both halves
        left = head
        right = prev

        while right:  
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True