bool dfs(int i, int j, vector<vector<char>>& grid){
            if(grid[i][j]=='1')
                grid[i][j]= 'N';
            else
                return false;
            if(i<grid.size()-1 && grid[i+1][j]=='1') dfs(i+1,j,grid);
            if(i>0 && grid[i-1][j]=='1') dfs(i-1,j,grid);
            if(j<grid[0].size()-1 && grid[i][j+1]=='1') dfs(i,j+1,grid);
            if(j>0 && grid[i][j-1]=='1') dfs(i,j-1,grid);
            return true;
        }  
int numIslands(vector<vector<char>>& grid) {
    int count = 0;
    for(int i = 0;i < grid.size(); i++){
        for(int j = 0; j < grid[0].size(); j++){
            if(dfs(i, j, grid))
                count++;
        }
    }
    return count;
}