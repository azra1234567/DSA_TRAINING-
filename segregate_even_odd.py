class Solution:
    def segregateEvenOdd(self, arr):
        evens = []
        odds = []

        for x in arr:
            if x % 2 == 0:
                evens.append(x)
            else:
                odds.append(x)

        evens.sort()
        odds.sort()

        k = 0
        for x in evens:
            arr[k] = x
            k += 1

        for x in odds:
            arr[k] = x
            k += 1