
import pygame, sys, consts

import soldier, game_field, screen as scr



def main():

    pygame.init()

    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

    pygame.display.set_caption("The Flag")

    clock = pygame.time.Clock()



    #

    player = soldier.create_soldier()

    field = game_field.create_game_field()

    screen_manager = scr.create_screen_manager(screen)



    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:

                    soldier.move_soldier(player, 1, 0)

                elif event.key == pygame.K_LEFT:

                    soldier.move_soldier(player, -1, 0)

                elif event.key == pygame.K_UP:

                    soldier.move_soldier(player, 0, -1)

                elif event.key == pygame.K_DOWN:

                    soldier.move_soldier(player, 0, 1)



        # draw

        scr.draw_background(screen_manager)

        soldier.draw_soldier(screen, player)


        scr.draw_message(screen_manager, "Welcome to The Flag game", pos=(40, 20))
        scr.draw_message(screen_manager,
                         "Have Fun!",
                         pos=(40, 40))
        scr.draw_message(screen_manager, "Welcome to The Flag game",
                         pos=(40, 20))
        scr.draw_message(screen_manager,
                         "Have Fun!",
        scr.draw_bushes(screen_manager)

        scr.draw_grid(screen_manager)




        pygame.display.flip()

        clock.tick(10)



    pygame.quit()

    sys.exit()


if __name__ == "__main__":
    main()


