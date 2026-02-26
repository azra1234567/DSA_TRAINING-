class Solution:
    def findKthPositive(self, arr, k):
        missing = 0
        cur = 1
        i = 0

        while True:
            if i < len(arr) and arr[i] == cur:
                i += 1
            else:
                missing += 1
                if missing == k:
                    return cur
            cur += 1