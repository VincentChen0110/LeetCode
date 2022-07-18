def goodNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.count = 0
    def check(root, val):
        if root:
            if root.val >= val:
                self.count += 1
            # else:
            #     val = root.val
            val = max(root.val, val)
            check(root.right, val)
            check(root.left, val)
        return
    check(root,root.val)

    return self.count
        