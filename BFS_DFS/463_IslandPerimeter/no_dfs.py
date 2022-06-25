def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res += 4*grid[i][j]
            if i>0: res -= grid[i-1][j]*grid[i][j]
            if j>0: res -= grid[i][j-1]*grid[i][j]
            if i<len(grid)-1: res -= grid[i+1][j]*grid[i][j]
            if j<len(grid[0])-1: res -= grid[i][j+1]*grid[i][j]
    return res
## Solution 2 here is faster since it only needs to consider 2 directions and decrease 2 each time
def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    ## if 2 blocks connect, total perimeter will decrease by 2
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1: 
                res+=4
                if i>0 and grid[i-1][j]==1: res-=2 #check top 
                if j>0 and grid[i][j-1]==1: res-=2 #check left
                ## lower and left havent been visited yet
                    
    return res