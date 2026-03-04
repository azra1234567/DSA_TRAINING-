class Solution:
    def longestCommonPrefix(self, words):

        if not words:
            return ""

        prefix = words[0]

        for w in words[1:]:
            while not w.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix