# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        numbers = []
        def addEm(node):
            nonlocal numbers
            if node:
                numbers.append(node.val)
                addEm(node.right)
                above = sum(i if i > node.val else 0 for i in numbers)
                node.val += above
                addEm(node.left)
                return node.val
            else:
                return 0
        addEm(root)
        return root