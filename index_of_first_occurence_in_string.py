class Solution:
    def strStr(self, s, t):
        if t == "":
            return 0
        
        n, m = len(s), len(t)

        for i in range(n - m + 1):
            if s[i:i+m] == t:
                return i
        
        return -1