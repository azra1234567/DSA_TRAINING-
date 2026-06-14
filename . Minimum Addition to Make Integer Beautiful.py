class Solution:
    def makeIntegerBeautiful(self, n, target):

        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        ans = 0
        power = 1

        while digit_sum(n) > target:
            ans += power * (10 - n % 10)
            n = n // 10 + 1
            power *= 10

        return ans
        