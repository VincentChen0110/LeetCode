def findCircleNum(self, isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """
    # O(n^2) DFS
#         n = len(isConnected)
#         ans = 0
    
#         def dfs(row, col):
#             if isConnected[row][col]!=1: return 
#             isConnected[row][col] = 2
#             isConnected[col][row] = 2
#             for i in range(n):
#                 if isConnected[row][i]==1:
#                     dfs(row, i)
#                 if isConnected[i][col]==1:
#                     dfs(i,col)
            
    
#         for i in range(n):
#             for j in range(n):
#                 if i==n/2 and j==n/2+1:
#                     break
#                 if isConnected[i][j]==1:
#                     ans+=1
#                     dfs(i,j)
#         return ans
    
    ## O(n) DFS
    n = len(isConnected)
    seen = set()
    ans = 0
    
    def dfs(node):
        for i, n in enumerate(isConnected[node]):
            if i not in seen and n:
                seen.add(i)
                dfs(i)
    for i in xrange(n):
        if i not in seen:
            ans += 1
            dfs(i)
    return ans