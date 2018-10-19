#write a function which returns all distinct
#nonattacking placements of n queens on an n x n
#chessboard, where n is an input to the program

# The expected output is a binary matrix which has 1s for the blocks where queens are placed. 

global N 
N=4
def isSafe(board, row, col): 
  
    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    # Check upper diagonal on left side 
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
        if board[i][j] == 1: 
            return False
  
    # Check lower diagonal on left side 
    for i,j in zip(range(row,N,1), range(col,-1,-1)): 
        if board[i][j] == 1: 
            return False
  
    return True
  
def solveNQUtil(board, col): 
    # base case: If all queens are placed 
    # then return true 
    if col == N:
        printSolution(board) 
        print '*********************'
        return True
  
    # Consider this column and try placing 
    # this queen in all rows one by one 
    res = False
    for i in range(N): 
  
        
        if isSafe(board, i, col): 
            # Place this queen in board[i][col] 
            board[i][col] = 1
  
            # recur to place rest of the queens 
            res = solveNQUtil(board, col+1) or res
              
   
                
  
            # If placing queen in board[i][col 
            # doesn't lead to a solution, then 
            # queen from board[i][col] 
            # print board
            board[i][col] = 0
            
    # if the queen can not be placed in any row in 
    # this colum col  then return false 
    return res
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print board[i][j], 
        print

def solveNQ(): 
    board = [ [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0] ]
   

    solveNQUtil(board, 0)


# driver program to test above function 
solveNQ() 
  

































#Matrix
# { 0,  0,  1,  0}
# { 1,  0,  0,  0}
# { 0,  0,  0,  1}
# { 0,  1,  0,  0}


# def n_queens(matrix, col):
    #if col >= N
    #     return true

    #iterating through each row in column
    # for i in range(n)
        #if safe call safe function
    #         board[i][col] = 1

    #         if n_queens(matrix, col+1)
    #             return true
    #     board[i][col] = 0
    # return false



 





# def n_queens(n):
#     def solve_n_queens(row):
#         if row == n:
#             # All queens are legally placed.
#             result.append(list(col_placement))
#             return
#         for col in range(n):
#             # Test if a newly placed queen will conflict any earlier queens
#             # placed before.
#             if all(
#                     abs(c - col) not in (0, row - i)
#                     for i, c in enumerate(col_placement[:row])):
#                 col_placement[row] = col
#                 solve_n_queens(row + 1)

#     result, col_placement = [], [0] * n
#     solve_n_queens(0)
#     return result

# print n_queens(4)