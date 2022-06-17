def isBalanced(self, root):
    stack, node, last, depths = [], root, None, {}
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(left - right) > 1: return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True