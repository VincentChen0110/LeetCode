# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 and root2): return (root1 or root2)
        queue1, queue2 = collections.deque([root1]), collections.deque([root2])
        while queue1 or queue2:
            n1, n2 = queue1.popleft(), queue2.popleft()
            if n1 and n2:
                n1.val = n1.val+n2.val
                if not n1.left and n2.left: n1.left = TreeNode(0)
                if not n1.right and n2.right: n1.right = TreeNode(0)
                queue1.append(n1.left)
                queue1.append(n1.right)
                queue2.append(n2.left)
                queue2.append(n2.right)
        return root1