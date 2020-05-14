# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
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