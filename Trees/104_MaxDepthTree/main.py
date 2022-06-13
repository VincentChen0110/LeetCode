# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):    
# Solution 1: 
        # if not root:return 0
        # tqueue, h = collections.deque(),0
        # tqueue.append(root)
        # while tqueue:
        #     nextlevel = collections.deque()
        #     while tqueue:
        #         front = tqueue.popleft()
        #         if front.left:
        #             nextlevel.append(front.left)
        #         if front.right:
        #             nextlevel.append(front.right)
        #     tqueue = nextlevel
        #     h += 1
        # return h
# Solution 2:
        # if root:
        #     return 1+max(self.maxDepth(root.right), self.maxDepth(root.left))
        # else:
        #     return 0
# Solution 3:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.right,depth+1), dfs(root.left,depth+1))
        return dfs(root, 0)
            