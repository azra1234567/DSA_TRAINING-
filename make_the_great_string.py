class Solution:
    def makeGood(self, s):
        stack = []

        for ch in s:
            if stack:
                top = stack[-1]
                if top.lower() == ch.lower() and top != ch:
                    stack.pop()
                    continue

            stack.append(ch)

        return "".join(stack)