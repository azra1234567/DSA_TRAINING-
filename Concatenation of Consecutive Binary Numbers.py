class Solution:
    def concatenatedBinary(self, n):
        arr = []
        
        for i in range(1, n+1):
            arr.append(bin(i)[2:])
        
        s = "".join(arr)
        return int(s,2) % 1000000007