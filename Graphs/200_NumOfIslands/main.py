def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        def dfs(row,col ,count):
            if grid[row][col] == "1":
                grid[row][col] = "2";
            else:
                return False;
            if(row < len(grid) - 1 and grid[row + 1][col] == "1"): dfs(row + 1, col,count)
            if(row > 0 and grid[row - 1][col] == "1"): dfs(row - 1, col,count)
            if(col < len(grid[0]) - 1 and grid[row][col + 1] =="1"): dfs(row, col + 1,count)
            if(col > 0 and grid[row ][col- 1] == "1"): dfs(row, col - 1,count)
            return True;
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(dfs(i,j,count)):
                    count+=1
                                                  
        return count
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(grid))