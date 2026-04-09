class Solution:
    def isSameTree(self, p, q):
        # both nodes are None
        if not p and not q:
            return True
        
        #  one node is None OR values differ
        if not p or not q or p.val != q.val:
            return False
        
        #  check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)