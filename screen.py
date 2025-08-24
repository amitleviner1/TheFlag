import pygame
import consts
import random

def create_screen_manager(screen):
    bush = pygame.image.load(consts.BUSH_IMG)
    bush = pygame.transform.scale(bush, (consts.CELL_SIZE, consts.CELL_SIZE))
    return {
        "screen": screen,
        "bush": bush,
        "bushes": [(random.randint(0, consts.COLS - 1),
                    random.randint(0, consts.ROWS - 1)) for _ in
                   range(consts.NUM_BUSHS)]
    }

def draw_background(manager):
    manager["screen"].fill(consts.GREEN)

def draw_bushes(manager):
    for col, row in manager["bushes"]:
        for i in range(20):
            px, py = col * consts.CELL_SIZE, row * consts.CELL_SIZE
            manager["screen"].blit(manager["bush"], (px, py))



def draw_grid(manager):
    for r in range(consts.ROWS):
        pygame.draw.line(manager["screen"], consts.BLACK, (0, r*consts.CELL_SIZE), (consts.WINDOW_WIDTH, r*consts.CELL_SIZE))
    for c in range(consts.COLS):
        pygame.draw.line(manager["screen"], consts.BLACK, (c*consts.CELL_SIZE, 0), (c*consts.CELL_SIZE, consts.WINDOW_HEIGHT))


def draw_message(manager, text, color=consts.WHITE, pos=(10, 10)):
    font = pygame.font.SysFont("Arial",16, bold = True)
    surface = font.render(text, True, color)
    manager["screen"].blit(surface, pos)

def show_message_and_wait(manager, text, seconds=3, color=consts.WHITE):
    draw_background(manager)
    draw_message(manager, text, color=color, pos=(200, consts.WINDOW_HEIGHT//2))
    pygame.display.flip()
    pygame.time.delay(seconds * 1000)

