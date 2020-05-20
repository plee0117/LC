# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        allofit = 0
        
        def atEach(node):
            nonlocal allofit
            if node:
                if not node.left and not node.right:
                    return node.val
                else:
                    if node.left:
                        left = atEach(node.left)
                    else:
                        left = 0
                    if node.right:
                        right = atEach(node.right)
                    else:
                        right = 0
                    allofit += abs(left - right)
                    return node.val + left + right
            return 0
        atEach(root)
        return allofit