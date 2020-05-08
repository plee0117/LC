# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val > q.val:
            p, q = q, p

        def check(node):
            nonlocal p, q
            if node.val < p.val:
                return check(node.right)
            elif node.val > q.val:
                return check(node.left)
            else:
                return node
            
        return check(root)