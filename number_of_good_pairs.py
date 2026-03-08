class Solution:
    def numIdenticalPairs(self, nums):
        count = {}
        ans = 0

        for n in nums:
            ans += count.get(n,0)
            count[n] = count.get(n,0) + 1

        return ans