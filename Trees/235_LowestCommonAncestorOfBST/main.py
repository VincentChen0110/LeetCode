def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    ## Soluton 1: Iterative
    # if not root or not p or not q: return None
    # if (max(p.val,q.val)<root.val):
    #     return self.lowestCommonAncestor(root.left,p,q)
    # elif(min(p.val,q.val)>root.val):
    #     return self.lowestCommonAncestor(root.right,p,q)
    # else:
    #     return root
    ## Solution 2: Recursive
    while root:
        if root.val > max(p.val,q.val):
            root = root.left
        elif root.val < min(p.val,q.val):
            root = root.right
        else:
            return root