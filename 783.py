# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        allofem = []
        def goThru(node):
            if node:
                nonlocal allofem
                allofem.append(node.val)
                goThru(node.left)
                goThru(node.right)
        goThru(root)
        allofem.sort()
        smallest = allofem[1] - allofem[0]
        for idx, val in enumerate(allofem[:-1]):
            smallest = min(allofem[idx + 1] - val, smallest)
        return smallest