from tictactoe import initial_state
import copy
import math

X = "X"
O = "O"
EMPTY = None

board = initial_state()

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_of_x = 0
    num_of_o = 0

    # calculate the quantity of X and O
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_of_x += 1
            elif board[i][j] == O:
                num_of_o += 1

    if num_of_x > num_of_o:
        return(O)
    else:
        return(X)


print("this is the move of", player(board))
#board[0][0] = X
print("this is the move of", player(board))

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    new_board = copy.deepcopy(board)
    move = player(board)
    if new_board[action[0]][action[1]] == None:
        new_board[action[0]][action[1]] = move
        return new_board
    else:
        raise NameError('Not valid action')



def winner(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                #check diagonals
                if i == 0 and j == 0:
                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2]:
                        return(board[i][j])
                
                if i == 0 and j == 2:
                    if board[i][j] == board[i+1][j-1] == board[i+2][j-2]:
                       return(board[i][j])
                #check horizontal rows
                try:
                    if board[i][j] == board[i][j+1] == board[i][j+2]:
                        return(board[i][j])

                except IndexError:
                    pass
                #check vertical rows     
                try:
                    if board[i][j] == board[i+1][j] == board[i+2][j]:
                        return(board[i][j])     
                except IndexError:
                    pass
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    return(False)
    return(True)

print(terminal(board))

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    tmp = winner(board)
    if tmp == X:
        return(1)
    elif tmp == O:
        return(-1)
    else:
        return(0)



def min_value(state):
    v = 2
    if terminal(state):
        return(utility(state))
    
    for move in actions(state):
        #print(result(state, move))
        v = min(v, max_value(result(state, move)))
        return v

        

def max_value(state):
    v = -2
    if terminal(state):
        return(utility(state))
    
    for move in actions(state):
        #print(result(state, move))
        v = max(v, min_value(result(state, move)))
        return v
        
        
board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
print(board)
print(player(board))
print("min value of board is", min_value(board))
print("max value of board is", max_value(board))

for move in actions(board):
    print("min value of board is", min_value(result(board, move)))
    print("max value of board is", max_value(result(board, move)))












"""
1. get a list of all possible actions
2. create a list of all possible boards after taking this actions
3. calculate the "score" of those boards. If you are X, use max function
4. if the "score" of the board suffice you, return it
"""

"""
example = [2,3,4]

def func(num):
    number = num*num
    if number > 100:
        print(number)
        return(number)
    print(number)
    return(func(number))

for i in example:
    print(func(i))
    """