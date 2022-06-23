# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            self.ans = max(self.ans,left+right)
            return 1+max(left,right)
        dfs(root)
        return self.ans