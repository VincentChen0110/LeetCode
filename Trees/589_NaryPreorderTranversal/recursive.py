def preorder(self, root):
    """
    :type root: Node
    :rtype: List[int]
    """
    res = []

    def dfs(root):
        if not root:
            return
        res.append(root.val)
        for child in root.children:
            dfs(child)
        return

    dfs(root)
    return res