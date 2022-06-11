grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

################### TIME COMPLEXITY #################
# Time complexity of dfs is to use stack and tranverse through the whole grid O(m * n)
################### SPACE COMPLEXITY ################
# Space complexity of dfs is to use stack with O (m * n)

# CodingStyle 1:
def maxAreaOfIsland(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        ans = 0
        ## Coding Style 1
        def dfs(x, y):
            if (0 <= x < row and 0 <= y < col and grid[x][y] == 1): 
                grid[x][y] = 0
                return dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1) + 1
            return 0

        ## Coding Style 2
        def dfs2(r, c):
            if r < 0 or r == row or c < 0 or c == col or grid[r][c] == 0: 
                return 0
            ans = 1
            grid[r][c] = 0  # Mark this square as visited
            DIR = [0, 1, 0, -1, 0]
            for i in range(4):
                ans += dfs(r + DIR[i], c + DIR[i + 1])
            return ans
        
        for i, item1 in enumerate(grid):
            for j, item2 in enumerate(item1):
                ans = max(ans,dfs(i,j))
        return ans



print(maxAreaOfIsland(grid))