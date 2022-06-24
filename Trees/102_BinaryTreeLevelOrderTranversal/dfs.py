# Time Complexity: O(N)
# Space Complexity: O(N) + O(h) for stack space
def levelOrder(self, root):
    result = []
    self.helper(root, 0, result)
    return result

def helper(self, root, level, result):
    if root is None:
        return
    if len(result) <= level:
        result.append([])
    result[level].append(root.val)
    self.helper(root.left, level+1, result)
    self.helper(root.right, level+1, result)
