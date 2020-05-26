# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(s, t):
            if s.val == t.val:
                if s.left and t.left:
                    left = isSame(s.left, t.left)
                elif not s.left and not t.left:
                    left = True
                else:
                    return False
                if s.right and t.right:
                    right = isSame(s.right, t.right)
                elif not s.right and not s.right:
                    right = True
                else:
                    return False
                return left and right
            else:
                return False
        if s:
            if isSame(s, t):
                return True
            else:
                if s.left and s.right:
                    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
                elif s.left:
                    return self.isSubtree(s.left, t)
                elif s.right:
                    return self.isSubtree(s.right, t)
                else:
                    return False
        return False