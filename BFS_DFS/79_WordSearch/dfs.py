 
def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(i, j,word,board):
                    return True
        return False
def dfs(self,i, j, word, board):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or word[0]!=board[i][j]:
        return False
    board[i][j] = "~"
    res = self.dfs(i+1, j, word[1:],board) or self.dfs(i-1, j, word[1:],board) or self.dfs(i, j+1, word[1:],board) or self.dfs( i, j-1, word[1:],board)
    board[i][j] = word[0]
    return res
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board,word))