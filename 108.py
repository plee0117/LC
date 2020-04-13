# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def makeLeft(l, r, node):
            m = (l + r) // 2
            node.left = TreeNode(nums[m])
            if l < m:
                makeLeft(l, m - 1, node.left)
            if m < r:
                makeRight(m + 1, r, node.left)

        def makeRight(l, r, node):
            m = (l + r) // 2
            node.right = TreeNode(nums[m])
            if l < m:
                makeLeft(l, m - 1, node.right)
            if m < r:
                makeRight(m + 1, r, node.right)
                
        l = len(nums)
        mid = l // 2
        if l == 0:
            return None
        else:
            start = TreeNode(nums[mid])
            if mid > 0:
                makeLeft(0, mid - 1, start)
            if mid < l - 1:
                makeRight(mid + 1, l - 1, start)
            return start