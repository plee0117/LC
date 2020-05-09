# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        s = 0
        def doThis(node, side):
            nonlocal s
            if node.left:
                doThis(node.left, -1)
            if node.right:
                doThis(node.right, 1)
            if not node.left and not node.right:
                if side == -1:
                    s += node.val
        if root:
            doThis(root,0)
        return s
