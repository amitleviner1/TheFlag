import random
import consts

EMPTY = 0
MINE = 1
FLAG = 2

def create_game_field():
    board = [[EMPTY for _ in range(consts.COLS)] for _ in range(consts.ROWS)]
    flag_pos = place_flag(board)
    place_mines(board)
    return {
        "board": board,
        "flag_pos": flag_pos
    }

def place_flag(board):
    start_row = consts.ROWS - 3
    start_col = consts.COLS - 4
    for i in range(3):
        for j in range(4):
            board[start_row + i][start_col + j] = FLAG
    return start_row, start_col

def place_mines(board):
    for _ in range(consts.NUM_MINES):
        r = random.randint(0, consts.ROWS - 1)
        c = random.randint(0, consts.COLS - 3)
        for j in range(3):
            board[r][c + j] = MINE