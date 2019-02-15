"""
Autor: Jesus Alberto Rodriguez Henao
"""

import sys
from math import pow


def validations(n, k, r_q, c_q, obstacles):
    n_flag = n > 0 and n <= int(pow(10, 5))
    k_flag = k >= 0 and k <= int(pow(10, 5))
    if not n_flag or not k_flag:
        return 'board dimensions or obstacles out of limits'
    else:
        if len(obstacles) != k and len(obstacles) != 0:
            return 'number of obstacles is not coincident with the given'
        elif len(obstacles) == k:
            q_rc = [r_q, c_q]
            for i in obstacles:
                if q_rc == i:
                    return 'queen and obstacle are in the same position'
        return True


def queensAttack(n, k, r_q, c_q, obstacles):
    # intializing the board
    # populate with ' ': void; '&': queen 'X': obstacle;
    board = [[' ' for j in range(0, n + 2)] for i in range(0, n + 2)]
    board[r_q][c_q] = '&'
    for i, j in obstacles:
        board[i][j] = 'X'

    diag = [[0, 0], [0, 0]]
    line = [[0, 0], [0, 0]]

    for i in range(1, n + 1):
        # to diagonals
        factor = r_q - i
        if c_q - factor > 0 and c_q - factor < n + 1:
            if diag[0][1] != 2:
                if board[i][c_q - factor] == ' ':
                    diag[0][0] += 1
                    board[i][c_q - factor] = 'O'
                elif board[i][c_q - factor] == '&':
                    diag[0][1] = 1
                else:
                    if diag[0][1] == 0:
                        diag[0][0] = 0
                    else:
                        diag[0][1] = 2

        if c_q + factor > 0 and c_q + factor < n + 1:
            if diag[1][1] != 2:
                if board[i][c_q + factor] == ' ':
                    diag[1][0] += 1
                    board[i][c_q + factor] = 'O'
                elif board[i][c_q + factor] == '&':
                    diag[1][1] = 1
                else:
                    if diag[1][1] == 0:
                        diag[1][0] = 0
                    else:
                        diag[1][1] = 2
        # to lines
        if i != r_q:
            if line[0][1] != 2:
                if board[i][c_q] == ' ':
                    line[0][0] += 1
                    board[i][c_q] = 'O'
                elif board[i][c_q] == '&':
                    line[0][1] = 1
                else:
                    if line[0][1] == 0:
                        line[0][0] = 0
                    else:
                        line[0][1] = 2
        else:
            for j in range(1, n + 1):
                if line[1][1] != 2:
                    if board[i][j] == ' ':
                        line[1][0] += 1
                        board[i][j] = 'O'
                    elif board[i][j] == '&':
                        line[1][1] = 1
                    else:
                        if line[1][1] == 0:
                            line[1][0] = 0
                        else:
                            line[1][1] = 2

    for i in reversed(board):
        print(i)

    sum = diag[0][0] + diag[1][0] + line[0][0] + line[1][0]
    return sum


if __name__ == "__main__":
    file = sys.argv[1]
    lines = []
    with open(file) as f:
        lines = f.readlines()
        lines = [[int(y) for y in x.strip().split(' ')] for x in lines]

    result = validations(
        lines[0][0],
        lines[0][1],
        lines[1][0],
        lines[1][1],
        lines[2:]
    )

    if result is True:
        moves = queensAttack(
            lines[0][0],
            lines[0][1],
            lines[1][0],
            lines[1][1],
            lines[2:]
        )
        print('movimientos: ', moves)
    else:
        print(result)
