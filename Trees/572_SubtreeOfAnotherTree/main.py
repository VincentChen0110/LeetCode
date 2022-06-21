# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not t: return True
        if not s: return False
        if s.val == t.val and self.checkSubtree(s, t):return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def checkSubtree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        if s.val != t.val: return False
        return self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right)