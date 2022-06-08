# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution 1 Recursive
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val==right.val:
            return self.isMirror(left.left,right.right) and self.isMirror(right.left, left.right)


# Solution2 Iterative
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        stack = [(root.left,root.right)]
        while stack:
            cur = stack.pop()
            l, r = cur[0], cur[1]
            if l is None and r is None: continue
            if l is None or r is None: return False
            if l.val!=r.val: return False
            stack.append((l.right, r.left))
            stack.append((l.left,r.right))
        return True