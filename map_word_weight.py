class Solution:
    def mapWordWeights(self, words, weights):
        letters = "abcdefghijklmnopqrstuvwxyz"
        ans = ""

        for word in words:
            total = 0

            for ch in word:
                total += weights[letters.index(ch)]

            ans += letters[25 - (total % 26)]

        return ans