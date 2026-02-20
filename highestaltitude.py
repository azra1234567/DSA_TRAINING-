class Solution:
    def largestAltitude(self, gain):
        cur = 0
        mx = 0
        
        for g in gain:
            cur += g
            mx = max(mx, cur)
        
        return mx