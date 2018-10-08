def initialise(board,n):
    for k in ['row','col','queen','nw_to_se','sw_to_ne']:
        board[k]={}
    for j in range(n):
        board['row'][j]=0
        board['col'][j]=0
        board['queen'][j]=-1
    for j in range(-(n-1),n):           #C-R = j , -7 is differencwe of 0 column 7 th row
        board['nw_to_se'][j]=0
    for j in range(2*n-1):
        board['sw_to_ne'][j]=0

def placequeen(i,board):
    n=len(board['queen'].keys())
    for j in range(n):
        if free(i,j,board):
            addqueen(i,j,board)
            if i == n-1:
                return True
            else:
                extends_solution = placequeen(i+1,board)
            if extends_solution:
                return True
            else :
                undoqueen(i,j,board)
    else:
        return False



def free(i,j,board):
    return (board['row'][i]==0 and board['col'][j]==0 and board['nw_to_se'][j-i]==0 and board['sw_to_ne'][j+i]==0)

def addqueen(i,j,board):
    board['row'][i]=1
    board['col'][j]=1
    board['queen'][i]=j
    board['nw_to_se'][j-i]=1
    board["sw_to_ne"][i+j]=1


def undoqueen(i,j,board):
    board['row'][i] = 0
    board['col'][j] = 0
    board['queen'][i] = -1
    board['nw_to_se'][j - i] = 0
    board["sw_to_ne"][i + j] = 0

def printboard(board):
    for i in sorted(board['queen'].keys()):
        print (i,board['queen'][i])

board={}
n= int(input("enter no:of queens"))
initialise(board,n)
if placequeen(0,board):
    printboard(board)
