#Time: O(N) | Space: O(size of return array + size of queue) -> Worst Case O(2N)
def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    queue, result = deque([root]), []
    
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result