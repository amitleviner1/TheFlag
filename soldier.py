import pygame
import consts

def create_soldier():
    img = pygame.image.load(consts.SOLDIER_IMG)
    img = pygame.transform.scale(img, (2 * consts.CELL_SIZE, 4 * consts.CELL_SIZE))
    return {
        "image": img,
        "x": 0,
        "y": 0
    }

def move_soldier(soldier, dx, dy):
    new_x = soldier["x"] + dx
    new_y = soldier["y"] + dy
    if 0 <= new_x <= consts.COLS - 2 and 0 <= new_y <= consts.ROWS - 4:
        soldier["x"] = new_x
        soldier["y"] = new_y

def draw_soldier(screen, soldier):
    px = soldier["x"] * consts.CELL_SIZE
    py = soldier["y"] * consts.CELL_SIZE
    screen.blit(soldier["image"], (px, py))

def get_body_indices(soldier):
    return [(soldier["y"] + i, soldier["x"] + j) for i in range(0, 3) for j in range(2)]

def get_feet_indices(soldier):
    return [(soldier["y"] + 3, soldier["x"]), (soldier["y"] + 3, soldier["x"] + 1)]
