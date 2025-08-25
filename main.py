import pygame, sys, consts

import soldier, game_field, screen as scr

def main():

    pygame.init()
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("The Flag")
    clock = pygame.time.Clock()

    player = soldier.create_soldier()
    field = game_field.create_game_field()
    screen_manager = scr.create_screen_manager(screen)

    running = True
    game_over = False
    message = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_RIGHT:
                    soldier.move_soldier(player, 1, 0)
                elif event.key == pygame.K_LEFT:
                    soldier.move_soldier(player, -1, 0)
                elif event.key == pygame.K_UP:
                    soldier.move_soldier(player, 0, -1)
                elif event.key == pygame.K_DOWN:
                    soldier.move_soldier(player, 0, 1)

                elif event.key == pygame.K_RETURN:
                    #  מציג רשת + מוקשים לשנייה אחת
                    scr.draw_background(screen_manager)
                    scr.draw_grid(screen_manager)
                    scr.draw_mines(screen_manager, field["mine_cells"])

                    pygame.display.flip()

                    pygame.time.wait(1000)

        if not game_over:
            if game_field.check_mine_touch(soldier.get_feet_indices(player), field):
                message = "Game Over! You hit a mine!"
                game_over = True
            elif game_field.check_flag_touch(soldier.get_body_indices(player), field):
                message = "You Win! Congratulations!"
                game_over = True

        scr.draw_background(screen_manager)
        scr.draw_bushes(screen_manager)
        soldier.draw_soldier(screen, player)

        if not game_over:
            scr.draw_message(screen_manager, "Welcome to The Flag game", pos=(40, 20))
            scr.draw_message(screen_manager,"Have Fun!", pos=(40, 40))
        else:
            scr.draw_message(screen_manager, message, pos=(200, consts.WINDOW_HEIGHT//2))

        pygame.display.flip()

        clock.tick(10)
        if game_over:
            pygame.time.delay(3000)
            running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()