"""If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an X, or 2 if it is an O, like so:

[[0,0,1],
 [0,1,2],
 [2,1,0]]
We want our function to return -1 if the board is not solved yet, 1 if X won, 2 if O won, or 0 if it's a cat's game (i.e. a draw)."""


def isSolved(board):
    a=row_check(board)
    if (a==1)|(a==2):
        return a
    else:
        b=col_check(board)
        if (b==1)|(b==2):
            return b
        else:
            c=diagnol_check(board)
            if (c==1)|(c==2):
                return c

    return -1


def row_check(board):
    a=[1 if i.count(1)==3 else 2 if i.count(0)==3 else 0 for i in board]
    if a.__contains__(1):
        return 1
    elif a.__contains__(2):
        return 2
    else :
        return -1

def col_check(board):
    for j in range(len(board)):
       a = []
       for i in board:
           a.append(i[j])
       if a.count(1)==3:
               return 1
       elif a.count(0)==3:
               return 2
    return -1
def diagnol_check(board):
    a=[board[i][j] for i in range(len(board)) for j in range(len(board)) if i==j]
    if a.count(1)==3:
        return 1
    if a.count(0)==3:
        return 0
    else :
        j=0;a=[]
        for i in range(2,-1,-1):
            a.append(board[i][j])
            j+=1
        if a.count(1) == 3:
            return 1
        if a.count(0) == 3:
            return 0
        else:
            return -1
