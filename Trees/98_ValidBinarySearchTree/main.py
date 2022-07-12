def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def dfs(root, left, right):
        if not root:
            return True
        if not left<root.val<right:
            return False
        return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
    return dfs(root, -float("inf"), float("inf"))