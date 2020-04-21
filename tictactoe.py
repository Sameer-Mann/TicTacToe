"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cx,co=0,0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='X':
                cx+=1
            elif board[i][j]=='O':
                co+=1
    if co==0 and cx==0:
        return 'X'
    elif co < cx:
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                a.append((i,j))
    return a

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]]!=EMPTY:
        raise NameError('InvalidAction')
    new_board=[list(board[i]) for i in range(3)]
    new_board[action[0]][action[1]]=player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i]==['X','X','X']:
            return 'X'
        elif board[i]==['O','O','O']:
            return 'O'

    # to check for 3X's or 3O's in all rows
    for j in range(3):
        col=[]
        for i in range(3):
            col.append(board[i][j])
        if col==['X','X','X']:
            return 'X'
        elif col==['O','O','O']:
            return 'O'
    diagonal=[]
    for i in range(3):
        diagonal.append(board[i][i])
    if diagonal==['X','X','X']:
        return 'X'
    elif diagonal==['O','O','O']:
        return 'O'
    diagonal=[]
    for i in range(3):
        diagonal.append(board[i][2-i])
    if diagonal==['X','X','X']:
        return 'X'
    elif diagonal==['O','O','O']:
        return 'O'
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win=winner(board)
    if win!=None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win=winner(board)
    if win=='X':
        return 1
    elif win=='O':
        return -1
    return 0

def f(pl,board,dp):
    if terminal(board):
        return (utility(board),None)
    state=(pl,str(board))
    # memorisation of states to prevent their recomputation
    if dp.get(state)!=None:
        return dp[state]
    if pl=='X':
        ans=-float('inf')
        move=None
        for action in actions(board):
            v=f('O',result(board,action),dp)
            # x player tries to choose the max possible ans
            if v[0]>ans:
                ans=v[0]
                move=action
        dp[state]=(ans,move)
        return dp[state]
    else:
        ans=float('inf')
        move=None
        for action in actions(board):
            v=f('X',result(board,action),dp)
            # o player tries to choose the min possible ans
            if v[0]<ans:
                ans=v[0]
                move=action
        dp[state]=(ans,move)
        return dp[state]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    pl=player(board)
    dp={}
    move = f(pl,board,dp)[1]
    # print(move)
    return move