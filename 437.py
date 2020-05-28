# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        out = 0
        
        def countem(path):
            nonlocal out, sum
            goal = 0
            for val in path[::-1]:
                goal += val
                if goal == sum:
                    out += 1

        def findpath(node, sofar):
            countem(sofar + [node.val])
            if node.left:
                findpath(node.left, sofar + [node.val])
            if node.right:
                findpath(node.right, sofar + [node.val])
                
        if root:
            findpath(root, [])
        return out