# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        biggest = {}
        def countEm(node):
            nonlocal biggest
            if node:
                if node.val in biggest:
                    biggest[node.val] += 1
                else:
                    biggest[node.val] = 1
                countEm(node.left)
                countEm(node.right)
        countEm(root)
        highest = 0
        out = []
        for idx, val in biggest.items():
            if val > highest:
                highest = val
                out = [idx]
            elif val == highest:
                out.append(idx)
        return out