from classes import *

pygame.init()

clock = pygame.time.Clock()
menu = Menu(init_menu_buttons(), init_menu_circles())
game_window = pygame.display.set_mode((WINDOW_SIZEX, WINDOW_SIZEY))
death_text1 = pygame.font.SysFont('arial', 100).render('YOU DIED', 10, BLACK)
death_text2 = pygame.font.SysFont('arial', 50).render('press any mousekey to continue', 10, BLACK)



while True:
    game_window.fill(WHITE)
    button = menu.check_mouse_pos()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()

        if i.type == pygame.MOUSEBUTTONUP and button:
            if button.text == 'play':
                ex = False
                game_over = False
                circles = init_game_circles()
                player = Player(WINDOW_SIZEX // 2, WINDOW_SIZEY // 2, 20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), '')

                while not ex:
                    game_window.fill(WHITE)

                    for i in pygame.event.get():
                        if i.type == pygame.QUIT:
                            quit()
                        if i.type == pygame.MOUSEBUTTONUP and game_over:
                            ex = True
                        if i.type == pygame.KEYUP:
                            player.dir = None

                    if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_d]:
                        player.dir = 'wd'
                    if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed()[pygame.K_s]:
                        player.dir = 'ds'
                    if pygame.key.get_pressed()[pygame.K_s]and pygame.key.get_pressed()[pygame.K_a]:
                        player.dir = 'sa'
                    if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_w]:
                        player.dir = 'aw'
                    if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed().count(1) == 1:
                        player.dir = 'w'
                    if pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed().count(1) == 1:
                        player.dir = 's'
                    if pygame.key.get_pressed()[pygame.K_d] and pygame.key.get_pressed().count(1) == 1:
                        player.dir = 'd'
                    if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed().count(1) == 1:
                        player.dir = 'a'

                    for i in circles:
                        if collide(player, i) and player.life_COUNT > 0:
                            if i.color == BLACK:
                                player.life_COUNT -= 1

                            if i.color == GREEN:
                                player.life_COUNT += 1

                            circles.append(Circle(random.randint(0, WINDOW_SIZEX), random.randint(-WINDOW_SIZEY, 0), 10, i.color, 'game'))
                            circles.remove(i)

                        i.move()
                        i.draw(game_window)

                    player.check_position()
                    player.draw(game_window)

                    interface = Interface(player.x, player.y, player.r, player.life_COUNT)
                    interface.draw(game_window)

                    if player.life_COUNT > 0:
                        player.move()
                    else:
                        game_window.blit(death_text1, (WINDOW_SIZEX//3, WINDOW_SIZEY//3))
                        game_window.blit(death_text2, (WINDOW_SIZEX // 3 - 90, 3 * WINDOW_SIZEY // 5))
                        game_over = True

                    clock.tick(FRAMES_PER_SECOND)
                    pygame.display.update()

            if button.text == 'exit':
                quit()

    if button:
        button.delta = 10
    else:
        for i in menu.buttons:
            i.delta = 0

    for i in menu.buttons:
        i.update()

    menu.draw_animation(menu.circles, game_window)

    for i in menu.circles:
        i.move()

    menu.draw(game_window)

    clock.tick(FRAMES_PER_SECOND)
    pygame.display.update()