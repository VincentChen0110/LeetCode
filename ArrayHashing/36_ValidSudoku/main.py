board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    ### ROW
    for item in board:
        num_list = [i for i in item if i!= "."]
        if len(set(num_list))!= len(num_list):
            #print("poop")
            return False
    ### COLUMN
    for item in zip(*board):
        num_list = [i for i in item if i!= "."]
        if len(set(num_list))!= len(num_list):
            #print("poop")
            return False

    ### check 3x3
    indexs = [(0,2,0,2),(3,5,0,2),(6,8,0,2),(0,2,3,5),(3,5,3,5),(6,8,3,5),(0,2,6,8),(3,5,6,8),(6,8,6,8)]
    for (starti,endi,startj,endj) in indexs:
        num_list = []
        for i in range(starti, endi+1):
            for j in range(startj, endj+1):
                if board[i][j]!= ".": num_list.append(board[i][j])
        #print(num_list)
        if len(set(num_list))!= len(num_list):
            #print("poop")
            return False
            
    return True
        



        
isValidSudoku(board)