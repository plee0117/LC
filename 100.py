# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSame(p, q):
            if p == None or q == None:
                if p == q:
                    return True
                else:
                    return False
            elif p.val != q.val:
                return False
            elif not isSame(p.right, q.right):
                return False
            elif not isSame(p.left, q.left):
                return False
            return True
        return isSame(p, q)