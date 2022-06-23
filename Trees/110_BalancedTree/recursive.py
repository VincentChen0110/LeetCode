## With Global Variable faster
def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            if abs(left-right)>1:self.res = False
            return 1+max(left, right)
        dfs(root)
        return self.res

## Without Global Variable slower
def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def getHeight(root):
        if not root: return 0
        left, right = getHeight(root.left), getHeight(root.right)
        return 1+max(left,right)
    
    if not root: return True
    return abs(getHeight(root.left)-getHeight(root.right))<=1 and isBalanced(root.left) and isBalanced(root.right)