# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        result = []
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
        dfs(root)
        return result
        