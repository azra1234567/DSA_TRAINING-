class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in last and last[s[r]] >= l:
                l = last[s[r]] + 1

            last[s[r]] = r
            ans = max(ans, r - l + 1)

        return ans