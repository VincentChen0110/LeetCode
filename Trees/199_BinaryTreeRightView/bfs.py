def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root == None: return []
    ans = []
    q = deque([root])
    while q:
        lastNode = None
        for _ in range(len(q)):
            cur = q.popleft()
            lastNode = cur
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)
        ans.append(lastNode.val)
    return ans