## Test 226: InvertBinaryTree
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
def invertTree(root):
    if root:
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
    return root

### Test 104: MaxDepthOfBinaryTree
# Input: root = [3,9,20,null,null,15,7]
# Output: 3 

def maxDepth(root):
    if root:
        return 1+max(maxDepth(root.left),maxDepth(root.right))
    else: return 0 

### TEST 543. Diameter of Binary Tree
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
def diameterOfBinaryTree(root):
    self.ans = 0
    def dfs(root):
        if not root: return 0
        left, right = dfs(root.left), dfs(root.right)
        self.ans = max(self.ans,left+right)
        return 1+max(left,right)
    dfs(root)
    return self.ans

# Test 110. Balanced Binary Tree
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
# Input: root = [3,9,20,null,null,15,7]
# Output: true
def isBalanced(root):
    self.res = True
    def dfs(root):
        if not root: return 0
        left,right = dfs(root.left),dfs(root.right)
        if abs(left-right)>1:
            self.res = False
        return 1+max(left,right)
    dfs(root)
    return self.res

