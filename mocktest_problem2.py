__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
You are given a placement of queens on a nxn board in which there is exactly one queen in each row and column.

Input representation (board) is a list of queen column positions (ie) if board[i] = j. It means queen in
ith column is placed in jth row. For nxn chessboard, you have rows 0..n-1 and cols 0..n-1.

Given a board, we define equivalent boards as placements obtained by:

1. Rotating the original by 90, 180 or 270 degrees clockwise.
2. Taking a mirror reflection of each of those rotations (including the original) assuming mirror
   is to the right

So you can get 8 equivalent boards (including original). Some of these can be duplicates as shown below.

E.x. if board = [0, 1, 2] it is equivalent to following chessboard - left bottom is
(0, 0):

_ _ Q    |
_ Q _    |
Q _ _    |

90 degree clockwise rotation of above board is

Q _ _
_ Q _
_ _ Q

Right Mirror reflection is:

Q _ _
_ Q _
_ _ Q

In the above case mirror reflection is same as 90 degree rotation, but that is not always the case.

Your job is to get unique equivalents for a given board position (filter out duplicates).

Additional notes:
1. Assume inputs are of valid type and content (ie) positions are valid too (one queen in every column and row).
2. Return a list of unique equivalent boards without repetitions. You could end up anywhere from 1 to 8 boards.
3. Hint: 180 deg rotation is 2 90 degree rotations, 270 is 3 90 deg rotations.
'''
def rotation_90(board):
   board={i:board[i] for i in xrange(len(board))}
   board={board[i]:(len(board)-1-i) for i in xrange(len(board))}
   board=[board[i] for i in xrange(len(board))]
   return board

def rotation_180(board):
    board=rotation_90(board)
    board=rotation_90(board)
    return board

def rotation_270(board):
    board = rotation_90(board)
    board = rotation_90(board)
    board = rotation_90(board)
    return board


def reflex(board):
    board=[len(board)-i-1 for  i in xrange(len(board))]
    return board

def get_equivalents(board):
   possible_pairs=[]
   possible_pairs.append(rotation_90(board))
   possible_pairs.append(rotation_180(board))
   possible_pairs.append(rotation_270(board))
   possible_pairs.append(board)
   for i in xrange(4):
       possible_pairs.append(reflex(possible_pairs[i]))
   print  possible_pairs


#write your own tests

def test_equivalents():
   get_equivalents([0,1,2,3])



