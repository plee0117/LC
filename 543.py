# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(node):
            if node.left == None:
                left, lmax = 0, 0
            else:
                left, lmax = depth(node.left)
            if node.right == None:
                right, rmax = 0, 0
            else:
                right, rmax = depth(node.right)
            return max(left, right) + 1, max(left + right, lmax, rmax)
        
        if root == None:
            return 0
        else:
            return depth(root)[1]