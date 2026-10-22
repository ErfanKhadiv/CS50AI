"""
Tic Tac Toe Player
"""

import math
import random
from copy import deepcopy

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

    X_count = 0
    O_count = 0
    EMPTY_count = 0

    for row in board:
      X_count += row.count(X)
      O_count += row.count(O)
      EMPTY_count += row.count(EMPTY)

    if X_count > O_count:
      return O
    else:
      return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    """

    moves = set()

    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i = action[0]
    j = action[1]

    # Check move is valid:
    if i not in [0, 1, 2] or j not in [0, 1, 2]:
      raise Exception('Result function given an invalid board position for action')
    elif board[i][j] != EMPTY:
      raise Exception('Result function tried to perform invalid action on occupaied tile')

    board_copy = deepcopy(board)
    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check Horizontal:
    for row in board:
      if row.count(X) == 3:
        return X
      if row.count(O) == 3:
        return O

    # Check Vertical:
    for j in range(3):
      column = ''
      for i in range(3):
        column += str(board[i][j])

      if column == 'XXX':
        return X
      if column == 'OOO':
        return O

    # Check Diagonals:
    diag1 = ''
    diag2 = ''
    j = 2

    for i in range(3):
      diag1 += str(board[i][i])
      diag2 += str(board[i][j])
      j -= 1

    if diag1 == 'XXX' or diag2 == 'XXX':
      return X
    elif diag1 == 'OOO' or diag2 == 'OOO':
      return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) or not actions(board):
      return True
    else:
      return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == 'X':
      return 1
    elif winner(board) == 'O':
      return -1
    else:
      return 0

actions_explored = 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    'X' Player is trying to maximise the score, 'O' Player is trying to minimise it
    """

    global actions_explored
    actions_explored = 0

    def max_player(board, best_min = 10):
      """ Helper function to maximise score for 'X' player.
          Uses alpha-beta pruning to reduce the state space explored.
          best_min is the best result
      """

      global actions_explored

      # If the game is over, return board value
      if terminal(board):
        return (utility(board), None)

      # Else pick the action giving the max value when min_player plays optimally
      value = -10
      best_action = None


      # Get set of actions and then select a random one until list is empty:
      action_set = actions(board)

      while len(action_set) > 0:
        action = random.choice(tuple(action_set))
        action_set.remove(action)

        # A-B Pruning skips calls to min_player if lower result already found:
        if best_min <= value:
          break

        actions_explored += 1
        min_player_result = min_player(result(board, action), value)
        if min_player_result[0] > value:
          best_action = action
          value = min_player_result[0]

      return (value, best_action)


    def min_player(board, best_max = -10):
      """ Helper function to minimise score for 'O' player """

      global actions_explored

      # If the game is over, return board value
      if terminal(board):
        return (utility(board), None)

      # Else pick the action giving the min value when max_player plays optimally
      value = 10
      best_action = None

      # Get set of actions and then select a random one until list is empty:
      action_set = actions(board)

      while len(action_set) > 0:
        action = random.choice(tuple(action_set))
        action_set.remove(action)

        # A-B Pruning skips calls to max_player if higher result already found:
        if best_max >= value:
          break

        actions_explored += 1
        max_player_result = max_player(result(board, action), value)
        if max_player_result[0] < value:
          best_action = action
          value = max_player_result[0]

      return (value, best_action)


    # If the board is terminal, return None:
    if terminal(board):
      return None

    if player(board) == 'X':
      print('AI is exploring possible actions...')
      best_move = max_player(board)[1]
      print('Actions explored by AI: ', actions_explored)
      return best_move
    else:
      print('AI is exploring possible actions...')
      best_move = min_player(board)[1]
      print('Actions explored by AI: ', actions_explored)
      return best_move