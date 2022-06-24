def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    self.row, self.col = len(board), len(board[0])
    self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(self.row):
        self.dfs(board,i,0)
        self.dfs(board,i,self.col-1)
    for i in range(self.col):
        self.dfs(board,0,i)
        self.dfs(board,self.row-1,i)
    for i, j in product(range(self.row),range(self.col)):
        board[i][j] = "X" if board[i][j] != "T" else "O"
        
def dfs(self, board, i, j):
    if board[i][j]!='O':
        return
    board[i][j] = 'T'
    for dir in self.directions:
        x, y = i + dir[0], j + dir[1]
        if 0<=x<self.row and 0<=y<self.col:
            self.dfs(board, x, y)