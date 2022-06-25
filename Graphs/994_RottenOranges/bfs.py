def orangesRotting(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    queue, res, cnt1 = deque([]), 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                cnt1+=1 ##count 1s in grid
            if grid[i][j] == 2: 
                queue.append((i,j))
                
    while queue:
        ## Check for each level of binary tree 
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for (x, y) in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                    cnt1-=1 ##eliminate 1s that have become rotten
                    grid[x][y]=2
                    queue.append((x,y))
        res += 1
                
    if cnt1!=0: return -1
    else: return max(0,res-1)
        