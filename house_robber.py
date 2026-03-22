class Solution:
    def rob(self, nums):
        prev, curr = 0, 0

        for num in nums:
            temp = max(curr, prev + num)
            prev = curr
            curr = temp

        return curr