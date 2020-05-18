"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        longest = 0
        def goOn(node, l):
            nonlocal longest
            if node:
                longest = max(longest, l)
                for i in node.children:
                    goOn(i, l + 1)
        if root:
            goOn(root, 1)
        return longest