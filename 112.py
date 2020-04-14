# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def addem(node, sum, sofar):
            here = sofar + node.val
            if node.left == None and node.right == None:
                return here == sum
            elif node.left and node.right:
                return addem(node.left, sum, here) or addem(node.right, sum, here)
            else:
                if node.left:
                    return addem(node.left, sum, here)
                if node.right:
                    return addem(node.right, sum, here)
        if root == None:
            return False
        else:
            return addem(root, sum, 0)