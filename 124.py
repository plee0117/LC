# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        runsum = root.val
        def downhere(node):
            nonlocal runsum
            if node.left:
                left = downhere(node.left)
            else:
                left = 0
            if node.right:
                right = downhere(node.right)
            else:
                right = 0
            runsum = max(runsum, node.val + max(0, left) + max(0, right))
            return node.val + max(0, left, right)
        downhere(root)
        return runsum