# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def addNode(t1, t2 = None):
            node = TreeNode()
            if t1 and t2:
                node.val = t1.val + t2.val
                node.left = addNode(t1.left, t2.left)
                node.right = addNode(t1.right, t2.right)
            elif t1:
                node.val = t1.val
                node.left = addNode(t1.left)
                node.right = addNode(t1.right)
            elif t2:
                node.val = t2.val
                node.left = addNode(t2.left)
                node.right = addNode(t2.right)
            else:
                return None
            return node
        return addNode(t1, t2)