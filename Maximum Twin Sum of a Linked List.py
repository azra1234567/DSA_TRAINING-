class Solution:
    def pairSum(self, head):

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        left = 0
        right = len(nums) - 1
        ans = 0

        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -= 1

        return ans