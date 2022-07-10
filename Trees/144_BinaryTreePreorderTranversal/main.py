def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    def dfs(root):
        if root:
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    return res