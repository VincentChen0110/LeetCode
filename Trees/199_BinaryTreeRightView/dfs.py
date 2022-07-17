def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ans = []
    
    def solve(root, level):
        if root:
            if len(ans) == level:
                ans.append(root.val) ## If there is right, append right first
            solve(root.right,level+1)
            solve(root.left,level+1)
        
    solve(root, 0)
    return ans