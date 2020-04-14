# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(node):
            if node.left == None:
                left = 1
            elif depth(node.left):
                left =  1 + depth(node.left)
            else:
                return False
                
            if node.right == None:
                right = 1
            elif depth(node.right):
                right = 1 + depth(node.right)
            else:
                return False
            if left > right + 1 or right > left + 1:
                return False
            else:
                return max(left, right)

        if root:
            if root.left == None:
                left = 1
            elif depth(root.left):
                left = 1 + depth(root.left)
            else:
                return False                
            if root.right == None:
                right = 1
            elif depth(root.right):
                right = 1 + depth(root.right)
            else:
                return False                
            if left > right + 1 or right > left + 1:
                return False
            else:
                return True
        else:
            return True