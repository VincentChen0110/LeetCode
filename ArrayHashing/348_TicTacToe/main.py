class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        #self.board = [['N' for _ in range(n)] for _ in range(n)]
        self.check_row = [0]*n
        self.row_name = [0]*n
        self.check_col = [0]*n
        self.col_name = [0]*n
        self.check_diag = [0,0]
        self.diag_name = [0,0]
#     def check_win(self, board):
        ## O(n^2) solution
#         diag = []
#         diag_2 = []
#         for i in range(len(board)):
#             if not 'O' in board[i] and not 'N' in board[i]:
#                 return 1
#             if not 'X' in board[i] and not 'N' in board[i]:
#                 return 2
#             if not 'O' in zip(*board)[i] and not 'N' in zip(*board)[i]:
#                 return 1
#             if not 'X' in zip(*board)[i] and not 'N' in zip(*board)[i]:
#                 return 2
            
#             diag.append(board[i][i])
#             diag_2.append(board[i][len(board)-1-i])
            
#         if not 'O' in diag and not 'N' in diag:
#             return 1
#         if not 'O' in diag_2 and not 'N' in diag_2:
#             return 1
#         if not 'X' in diag and not 'N' in diag:
#             return 2
#         if not 'X' in diag_2 and not 'N' in diag_2:
#             return 2
            
#         return 0
   
            
        
    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if not self.check_row[row] or self.row_name[row]==player :
            self.check_row[row]+=1
            self.row_name[row] = player
            if self.check_row[row]==len(self.check_row):
                return player
            
        if not self.check_col[col] or self.col_name[col]==player :
            self.check_col[col]+=1
            self.col_name[col] = player
            if self.check_col[col]==len(self.check_col):
                return player
            
        if row==col:
            if not self.check_diag[0] or self.diag_name[0]==player :
                self.check_diag[0]+=1
                self.diag_name[0] = player
                if self.check_diag[0]==len(self.check_col):
                    return player
            
        if row+col==len(self.check_row)-1:
            if not self.check_diag[1] or self.diag_name[1]==player :
                self.check_diag[1]+=1
                self.diag_name[1] = player
                if self.check_diag[1]==len(self.check_col):
                    return player
        return 0
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)