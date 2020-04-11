# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(left, right):
            if left == None or right == None:
                if left == right:
                    return True
                else:
                    return False
            elif left.val != right.val:
                return False
            elif not compare(left.left, right.right):
                return False
            elif not compare(left.right, right.left):
                return False
            return True
        
        if root == None:
            return True
        else:
            return compare(root.left, root.right)