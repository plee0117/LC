# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def deep(node, depth, s):
            if node.right != None or node.left != None:
                if node.left:
                    s = deep(node.left, depth + 1, s)
                if node.right:
                    s = deep(node.right, depth + 1, s)
            else:
                if s == None:
                    s = depth
                else:
                    s = min(s, depth)
            return s
        if root == None:
            return 0
        else:
            return deep(root, 1, None)