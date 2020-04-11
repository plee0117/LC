# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(r, position):
            if r == None:
                return position + 1
            else:
                return max(depth(r.left, position + 1), depth(r.right, position + 1))
        if root == None:
            return 0
        else:
            return max(depth(root.right, 0), depth(root.left, 0))