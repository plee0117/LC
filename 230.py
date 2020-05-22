# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ct = 0
        def check(node):
            nonlocal ct, k
            if node.left:
                l = check(node.left)
                if l is not None:
                    return l
            ct += 1
            if ct == k:
                return node.val
            if node.right:
                r = check(node.right)
                if r is not None:
                    return r
        return check(root)