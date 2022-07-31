def hasPathSum(self, root, targetSum):
    """
    :type root: TreeNode
    :type targetSum: int
    :rtype: bool
    """
    if not root:return False
    self.res = False
    def dfs(root, ans):
        ans += root.val
        if ans==targetSum and not root.left and not root.right:
            self.res = True
        if root.right:dfs(root.right, ans)
        if root.left:dfs(root.left, ans)
    
    dfs(root, 0)
    return self.res