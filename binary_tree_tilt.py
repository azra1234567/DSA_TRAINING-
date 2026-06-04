class Solution:
    def findTilt(self, root):
        ans = [0]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left > right:
                ans[0] += left - right
            else:
                ans[0] += right - left

            return left + right + node.val

        dfs(root)
        return ans[0]