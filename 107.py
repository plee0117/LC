# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def goDeep(node, h = 0):
            if node == None:
                return
            else:
                if h in v:
                    v[h].append(node.val)
                else:
                    v[h] = [node.val]
            if node.left != None:
                goDeep(node.left, h + 1)
            if node.right != None:
                goDeep(node.right, h + 1)
                    
        v = dict()
        goDeep(root)
        key = list(v.keys())
        key.sort(reverse = True)
        return [v[k] for k in key]