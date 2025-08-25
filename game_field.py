import random
from inspect import stack

import consts

EMPTY = 0
MINE = 1
FLAG = 2

def create_game_field():
    board = [[EMPTY for _ in range(consts.COLS)] for _ in range(consts.ROWS)]
    flag_cells= place_flag(board)
    mine_cells = place_mines(board)
    place_mines(board)

    return {
        "board": board,
        # "flag_pos": flag_pos,
        "flag_cells": flag_cells,
        "mine_cells": mine_cells
    }

def place_flag(board):
    cells = []
    start_row = consts.ROWS - 3
    start_col = consts.COLS - 4
    for i in range(3):
        for j in range(4):
            board[start_row + i][start_col + j] = FLAG
            cells.append((start_row + i, start_col + j))
    return cells

def place_mines(board):
    cells = place_flag(board)
    mines = []
    for _ in range(consts.NUM_MINES):
        row = random.randint(0, consts.ROWS - 1)
        col = random.randint(0, consts.COLS - 3)
        for j in range(3):
            board[row][col + j] = MINE
            mines.append((row, col + j))
        cells.extend(mines)
    return cells

def check_flag_touch(soldier_body, field):
        for cell in soldier_body:
            if cell in field["flag_cells"]:
                return True
        return False

def check_mine_touch(soldier_feet, field):
    for cell in soldier_feet:
        if cell in field["mine_cells"]:
            return True
    return False