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