# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        out =[]
        def pathfind(node, path):
            nonlocal out
            path += str(node.val)
            if not (node.left or node.right):
                out.append(path)
            if node.left:
                pathfind(node.left, path + '->')
            if node.right:
                pathfind(node.right, path + '->')
                
        if root:
            pathfind(root, '')
        return out