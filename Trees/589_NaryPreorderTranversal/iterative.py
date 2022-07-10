def preorder(self, root):
    """
    :type root: Node
    :rtype: List[int]
    """
    res = []
    if not root:
        return []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        
        for child in node.children[::-1]:
            stack.append(child)
    return res